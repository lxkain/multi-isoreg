# Multiple Isotonic Regression

Given a sequence, this algorithm can find the minimum error and optimal inflection points of segments that are either monotonically rising or falling.
This allows finding shapes like up-down (one peak), or down-up-down, or up-down-up-down (2 peaks), etc.


## Installation

Change the directory to the `mir` subdirectory and type `make`. Afterwards, have a look at `main.py` for usage.


## Example

For example, consider the sequence

```
[  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.
  16.  17.  18.  19.  20.  19.  18.  17.  16.  15.  14.  13.  12.  11.  10.
  11.  12.  13.  14.  15.  16.  17.  18.  19.  20.  21.  22.  23.  24.  23.
  22.  21.  20.  19.  18.  17.  16.  17.  18.  17.  16.  15.  14.  13.  12.
  11.  10.   9.   8.]
```

which is known to have 5 inflection points.
After a call to `multi_isoreg()`, the overall error and inflection points are returned;
in this case the error is zero, and the inflection points are discovered at `[19 29 43 51 53]`,
optimally partitioning the sequence into upwards and downwards going segments

```
[  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.
  16.  17.  18.  19.]
[ 20.  19.  18.  17.  16.  15.  14.  13.  12.  11.]
[ 10.  11.  12.  13.  14.  15.  16.  17.  18.  19.  20.  21.  22.  23.]
[ 24.  23.  22.  21.  20.  19.  18.  17.]
[ 16.  17.]
[ 18.  17.  16.  15.  14.  13.  12.  11.  10.   9.   8.]
```


(c) 2017 Alexander Kain
