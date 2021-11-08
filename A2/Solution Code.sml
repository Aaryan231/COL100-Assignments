(* SUM OF 3 PRIMES *)

fun isPrime(n) =
  let fun helperIP(n, x) =
        if n = 1
        then false
        else if x*x > n andalso (x-1)*(x-1) <= n
             then true
             else if n mod x = 0
                  then false
                  else helperIP(n, x + 1)
  in helperIP(n, 2)
 end;

fun findPrimes(n) =
  let fun helperFP(n, x, y) =
        if n <= 5 orelse x = n
        then (0, 0, 0)
        else if isPrime(x) andalso isPrime(y) andalso isPrime(n - x - y)
             then (x, y, n - x - y)
             else if y = n
                  then helperFP(n, x + 1, x + 1)
                  else helperFP(n, x, y + 1)
  in if n mod 2 = 0 
     then helperFP(n, 2, 2)
     else helperFP(n, 3, 2)
  end;


(* PACKING THE DIKKI *)

fun max(a, b) =
  if a > b
  then a
  else b;

fun maximumValue(n, v, w, W) =
  let fun helperMV(n, v, w, W, c) =
        if W < 0
        then c - v(n+1)
        else if n = 0 orelse W = 0
             then c
             else max(helperMV(n - 1, v, w, W - w(n), c + v(n)), helperMV(n - 1, v, w, W, c))
  in helperMV(n, v, w, W, 0)
  end;


(* HUMAN-FRIENDLY UNITS *)

fun toString(n) =
  let fun helperTS(n) =
           if n = 0 then "0"
      else if n = 1 then "1"
      else if n = 2 then "2"
      else if n = 3 then "3"
      else if n = 4 then "4"
      else if n = 5 then "5"
      else if n = 6 then "6"
      else if n = 7 then "7"
      else if n = 8 then "8"
      else "9";
  in if n < 10
     then helperTS(n)
     else toString(n div 10) ^ helperTS(n mod 10)
  end;

fun convertUnitsRec(n, string, fac) =
  let fun helperCUR(n, string, fac, c) =
        if n < fac(c) orelse fac(c) = 0
        then toString(n) ^ " " ^ string(c)
        else helperCUR(n div fac(c), string, fac, c + 1) ^ " " ^ toString(n mod fac(c)) ^ " " ^ string(c);
  in helperCUR(n, string, fac, 0)
  end;

fun convertUnitsIter(n, string, fac) =
  let fun helperCUI(n, string, fac, c, output) =
          if n < fac(c) orelse fac(c) = 0
          then toString(n) ^ " " ^ string(c) ^ output
          else helperCUI(n div fac(c), string, fac, c+1, " " ^ toString(n mod fac(c)) ^ " " ^ string(c) ^ output);
  in helperCUI(n, string, fac, 0, "")
  end;


(* ITERATIVE INTEGER SQUARE ROOT *)

fun highest_power(n) =
  let fun helperHP(n, c) =
        if n div 4 = 0
        then c
        else helperHP(n div 4, 4 * c);
  in helperHP(n, 1)
  end;

fun intSqrt(n)=
let fun helperIS(n, high_pow, k)=
       if high_pow = 0
       then k
       else if (2*k + 1) * (2*k + 1) > n div high_pow
            then helperIS(n, high_pow div 4, 2*k)
            else helperIS(n, high_pow div 4, 2*k + 1)
in helperIS(n, highest_power(n), 0)
end;
