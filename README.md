# Overview [![Build Status](https://travis-ci.org/hailpam/pyfiql.svg?branch=main)](https://travis-ci.org/hailpam/pyfiql)
PyFiql...

## TBD

# Examples
## Example 1
Expression:
```bash
(((((product=="Apple",product=="Google");(name=="Joe",name=="Alan")));label=!~="text";(qty=gte=1,qty=lte=10)))
```

Generated Abstract Syntax Tree:
```bash
[ ; ]
        [ ; ]
                [ , ]
                        [product == "Apple"]
                        [product == "Google"]
                [ , ]
                        [name == "Joe"]
                        [name == "Alan"]
        [ ; ]
                [label =!~= "text"]
                [ , ]
                        [qty =gte= 1]
                        [qty =lte= 10]
```

## Example 2
Expression:
```bash
(product=="Apple",product=="Google");(name=="Joe",name=="Alan");(qty=gte=1,qty=lte=10)
```

Generated Abstract Syntax Tree:
```bash
[ ; ]
        [ , ]
                [product == "Apple"]
                [product == "Google"]
        [ ; ]
                [ , ]
                        [name == "Joe"]
                        [name == "Alan"]
                [ , ]
                        [qty =gte= 1]
                        [qty =lte= 10]
```

## Example 3
Expression:
```bash
(qty=gt=1;(qty=gte=1,qty=lte=10));(product=="Apple",product=="HP")
```

Generated Abstract Syntax Tree:
```bash
[ ; ]
        [ ; ]
                [qty =gt= 1]
                [ , ]
                        [qty =gte= 1]
                        [qty =lte= 10]
        [ , ]
                [product == "Apple"]
                [product == "HP"]
```

## Example 4
Expression:
```bash
(product=="Apple",qty=lt=1);name=="Joe"
```

Generated Abstract Syntax Tree:
```bash
[ ; ]
        [ , ]
                [product == "Apple"]
                [qty =lt= 1]
        [name == "Joe"]
```

## Example 5
Expression:
```bash
name==bar,dob=gt=1990-01-01
```

Generated Abstract Syntax Tree:
```bash
[ , ]
        [name == bar]
        [dob =gt= 1990-01-01]
```