(* 1.STAIR CLIMBING PROBLEM *)

fun climbStair(n) =
  if n = 1 orelse n = 0
  then 1
  else climbStair(n - 1) + climbStair(n - 2);


(* 2.PLAYING WITH DIGITS *)

fun pow(x, n) =
  if n = 0
  then 1
  else x * pow(x, n - 1);

fun modifiedDigitSum(n) =
  let fun helperMDS(n, x) =
        if n < 10
        then n * pow(2, x)
        else helperMDS(n div 10, x + 1) + (n mod 10)*pow(2, x)
  in helperMDS(n, 0)
  end;


(* 3.SUM OF SQUARES *)

fun SumOfSquares(n, x, y) =
  if n = x*x + y*y
  then true
  else if x = n
       then false
       else if y = n
            then SumOfSquares(n, x+1, x+1)
            else SumOfSquares(n, x, y+1);

fun squaredCount(n) =
  if n = 1
  then 1
  else if SumOfSquares(n, 0, 1)
       then 1 + squaredCount(n - 1)
       else squaredCount(n - 1);


(* 4.SUMMING A SERIES *)

fun abs(n) =
  if n >= 0.0
  then n
  else ~n;

fun termsForSum(n) =
  let val m = 2.0 * real(n)
  in if n mod 2 <> 0 
     then 4.0 * 1.0/(m) * 1.0/(m + 1.0) * 1.0/(m + 2.0) 
     else ~4.0 * 1.0/(m) * 1.0/(m + 1.0) * 1.0/(m + 2.0)
  end;

fun nilkanthaSum(n) =
  let fun helperNilkanthaSum(n: real, x) =
        if n >= 3.0
        then 3.0
        else if n > abs(termsForSum(x))
             then 3.0 + termsForSum(x)
             else helperNilkanthaSum(n, x + 1) + termsForSum(x)
  in  helperNilkanthaSum(n, 1)
  end;
