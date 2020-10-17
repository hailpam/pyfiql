# Overview [![Build Status](https://travis-ci.org/hailpam/pyfiql.svg?branch=main)](https://travis-ci.org/hailpam/pyfiql)
PyFiql is a versatile parser for the [Feed Item Query Language](https://tools.ietf.org/html/draft-nottingham-atompub-fiql-00). Once deserialized the string into an Abstract Syntax Tree (AST), the library provides the ability to re-serialize it in a number of custom formats leveraging a support based on the Visitor design pattern. An expression can be then transformed into filters for a traditional SQL database or any other NoSQL one (e.g. MongoDB or even Elasticsearch).

## About FIQL
The Feed Item Query Language (FIQL, pronounced "fickle") is a simple
but flexible, URI-friendly syntax for expressing filters across the
entries in a syndicated feed.  For example,

```bash
title==foo*;(updated=lt=-P1D,title==*bar)
```

will return all entries in a feed that meet the following criteria;

- have a title beginning with ```foo```, ```AND```
- have been updated in the last day ```OR``` have a title ending with
"bar".

This specification defines an extensible syntax for FIQL queries (in
Section 3), explains their use in HTTP (Section 4), and defines feed
extensions for discovering and describing query interfaces
(Section 5).

## Definitions
### Expressions
An FIQL expression is composed of one or more constraints, related to
each other with Boolean operators.

FIQL expressions yield Boolean values: True or False.

```
expression  = [ "(" ]
                ( constraint / expression )
                [ operator ( constraint / expression ) ]
                [ ")" ]
operator    = ";" / ","
```

- ```;``` is the Boolean AND operator; it yields True for a particular
entry if both operands evaluate to True, otherwise False.
- ```,``` is the Boolean OR operator; it yields True if either operand
evaluates to True, otherwise False.

By default, the AND operator takes precedence (i.e., it is evaluated
before any OR operators are).  However, a parenthesised expression
can be used to change precedence, yielding whatever the contained
expression yields.


### Constraints
A FIQL constraint is composed of a selector, which identifies a
portion of an entry's content, and an optional comparison/argument
pair, which refines the constraint.  When processed, a constraint
yields a Boolean value.

```
constraint  = selector [ comparison argument ]
selector    = 1*( unreserved / pct-encoded )
comparison  = ( ( "=" 1*ALPHA ) / fiql-delim ) "="
argument    = 1*arg-char
arg-char    = unreserved / pct-encoded / fiql-delim / "="
fiql-delim  = "!" / "$" / "'" / "*" / "+"
```

# Install, Build and Testing
Being a Python code base, there is no need to compile. Moreover, the library makes only use of base libaries, so there is no requirement to being installed prior to the usage.

## Init and Install
To init the project.

```bash
$> make init
```

## Testing
To test the project.

```bash
$> make test
```

# Usage
The examples folder contains concrete examples of how to run the library. Hereafter there are two major use cases.

## Create an In-Memory AST
To create a traversable AST:

```python
queries = [
    '(product=="Apple",qty=lt=1);name=="Joe"',
    'name==bar,dob=gt=1990-01-01'
]

for query in queries:
    print(query)
    root = parser.scan(query)
    util.pretty_printing(root, 0)
```

A prettified output from the AST traversal:

```bash
(product=="Apple",qty=lt=1);name=="Joe"
[ ; ]
        [ , ]
                [product == "Apple"]
                [qty =lt= 1]
        [name == "Joe"]
name==bar,dob=gt=1990-01-01
[ , ]
        [name == bar]
        [dob =gt= 1990-01-01]
```

## AST to Backend-specific Format 
To re-serialize the AST into a backend-specific format:

### SQL

```python
queries = [
    'name=="bar",date=gt=1990-01-01',
    '(product=="Apple",qty=lt=1);name=="Joe"',
]
for query in queries:
    root = parser.scan(query)
    visit = visitor.SqlVisitor()
    visitor.traversal(root, visit)
    print(visit.expressions)
```

An ouput printing out the re-serialized format:

```bash
name=="bar",date=gt=1990-01-01
['(name = "bar" OR date > 1990-01-01)']

(product=="Apple",qty=lt=1);name=="Joe"
['((product = "Apple" OR qty < 1) AND name = "Joe")']
```

### JSON (Polish Notation)

```python
queries = [
    'name=="bar",date=gt=1990-01-01',
    '(product=="Apple",qty=lt=1);name=="Joe"',
]

for query in queries:
    root = parser.scan(query)
    visit = visitor.JsonVisitor()
    visitor.traversal(root, visit)
    print(json.dumps(visit.expressions, indent=2))
```

An ouput printing out the re-serialized format:

```bash
name=="bar",date=gt=1990-01-01
[
  {
    "OR": [
      {
        "=": [
          "name",
          "\"bar\""
        ]
      },
      {
        ">": [
          "date",
          "1990-01-01"
        ]
      }
    ]
  }
]
(product=="Apple",qty=lt=1);name=="Joe"
[
  {
    "AND": [
      {
        "OR": [
          {
            "=": [
              "product",
              "\"Apple\""
            ]
          },
          {
            "<": [
              "qty",
              "1"
            ]
          }
        ]
      },
      {
        "=": [
          "name",
          "\"Joe\""
        ]
      }
    ]
  }
]
```
