(* COMMON HELPER FUNCTIONS FOR PROBLEM-1 *)

fun reverse([]) = []
  | reverse(x :: xs) = reverse(xs) @ [x];

fun simplify(ls) =
  let fun helperS(ls) =
        if null(ls)
        then ls
        else  if hd(ls) = 0
              then helperS(tl(ls))
              else reverse(ls)
  in helperS(reverse(ls))
  end;

fun operate(f, []) = []
  | operate(f, x :: xs) = f(x) :: operate(f, xs);


(* OPERATIONS ON VERY LARGE NUMBERS *)

fun LgintToInt(ls) =
  let fun helperLITI(ls, c, x) =
        if length(ls) >= 10
        then 1000000000
        else if null(ls)
             then c
             else helperLITI(tl(ls), c + x * hd(ls), 10 * x);
  in helperLITI(simplify(ls), 0, 1)
  end;

fun intToLgint(n) =
  let fun helperITLI(n, ls) =
        if n < 10
        then ls @ [n]
        else ls @ [n mod 10] @ helperITLI(n div 10, ls)
  in helperITLI(n, [])
  end;

fun addLgint(l1, l2) =
  let fun helperALI([], [], c, ls) = ls @ (if c = 0 then [] else [c])
        | helperALI([], y :: ys, c, ls) = helperALI([], ys, (y + c) div 10, ls @ [(y + c) mod 10])
        | helperALI(x :: xs, [], c, ls) = helperALI(xs, [], (x + c) div 10, ls @ [(x + c) mod 10])
        | helperALI(x :: xs, y :: ys, c, ls) = helperALI(xs, ys, (x + y + c) div 10, ls @ [(x + y + c) mod 10])
  in helperALI(simplify(l1), simplify(l2), 0, [])
  end;

fun LgLesseq(l1, l2) =
  let fun helperLLE(l1, l2) =
        if length(l1) < length(l2)
        then true
        else if length(l1) > length(l2)
             then false
             else if hd(l1) < hd(l2)
                  then true
                  else if hd(l1) > hd(l2)
                       then false
                       else helperLLE(tl(l1), tl(l2))
  in helperLLE(reverse(simplify(l1)), reverse(simplify(l2)))
  end;

fun multiplyLgint(l1, l2) =
  let fun scale(ls,a) =
        let fun helperM([]) = []
              | helperM([x]) =
                  if x >= 10
                  then (x mod 10) :: [x div 10]
                  else [x]
              | helperM(x :: y :: xs) =
                  if x >= 10
                  then (x mod 10) :: helperM((y + x div 10) :: xs)
                  else x :: helperM(y :: xs)
        in helperM(operate((fn n => n * a), ls))
        end;
     
     fun helperMLI(l1, l2, x, r) =
       if null(l2)
       then r @ (if null(r) then [0] else [])
       else helperMLI(l1, tl(l2), 0 :: x, addLgint(r, x @ scale(l1, hd(l2))))
  in helperMLI(simplify(l1), simplify(l2), [], [])
  end;


(* QUARTERLY PERFORMANCE *)

fun qPerformance(ls) =
  let fun element (a, b, c, d, e) x =
             if x = 0 then a
        else if x = 1 then b
        else if x = 2 then c
        else if x = 3 then d
        else e;
      
      fun salary (a, b, c, d, e) =
        e + ((a + b + c + d) * (e div 100));
      
      fun average([], c) = 0.0
        | average(x :: xs, c) =
             ((real(element x c)) / real(length(ls))) + average(xs, c);
      
      fun hike(ls) =
        let fun helperH((a,b,c,d,e)) = 
              (if real(a)>average(ls,0) then floor(100.0*(real(a)-average(ls, 0))/(10.0*average(ls, 0))) else 0,
               if real(b)>average(ls,1) then floor(100.0*(real(b)-average(ls, 1))/(10.0*average(ls, 1))) else 0,
               if real(c)>average(ls,2) then floor(100.0*(real(c)-average(ls, 2))/(10.0*average(ls, 2))) else 0,
               if real(d)>average(ls,3) then floor(100.0*(real(d)-average(ls, 3))/(10.0*average(ls, 3))) else 0, e)
        in map helperH ls
        end;
      
      fun new_salary([]) = []
        | new_salary(x :: xs) = [salary x] @ new_salary(xs);
  in new_salary(hike(ls))
  end;

fun budgetRaise(ls) =
  let fun add (a, b, c, d, e) =
        e;
      
      fun new_total([]) = 0
        | new_total(x :: xs) = x + new_total(xs);
      
      fun old_total([]) = 0
        | old_total(x :: xs) = (add x) + old_total(xs);
      
      fun fraction(x, y) =
        ((real(x) - real(y)) / real(y));
  in fraction(new_total(qPerformance(ls)), old_total(ls))
  end;


(* LEXICOGRAPHIC PERMUTATIONS *)

fun lexicographicPerm(ls) =
  let fun msort([]) = []
        | msort(x::[]) = x::[]
        | msort(ls) =
            let fun split(ls) =
                  let fun splititer([],i,l1,l2) = (l1,l2)
                        | splititer(x::ls,i,l1,l2) =
                            if (i mod 2 = 0) 
                            then splititer(ls,i+1,x::l1,l2)
                            else splititer(ls,i+1,l1,x::l2)
                  in splititer(ls,1,[],[])
                  end;
                
                fun merge([],l2) = l2
                  | merge(l1,[]) = l1
                  | merge(x::l1,y::l2) =
                      if x <= y
                      then x::merge(l1,y::l2)
                      else y::merge(x::l1,l2);
                
                val (l1,l2) = split(ls)
            in merge(msort(l1),msort(l2))
            end;
      
      fun cyclize(ls, i, x) =
        if i = 1
        then hd(ls) :: (x @ tl(ls))
        else cyclize(tl(ls), i - 1, x @ [hd(ls)]);
      
      fun cycle_list(ls, i, x) =
        if i = length(ls)
        then x @ [cyclize(ls, i, [])]
        else cycle_list(ls, i + 1, x @ [cyclize(ls, i, [])]);
      
      fun append([], a) = []
        | append(x :: xs, a) = [a :: x] @ append(xs, a);
      
      fun oper(ls, x, f) =
        if null(ls)
        then x
        else oper(tl(ls), x @ append(f(tl(hd(ls))), hd(hd(ls))), f);
      
      fun permutations(ls) =
        if length(ls) = 2
        then [ls, tl(ls) @ [hd(ls)]]
        else oper(cycle_list(ls, 1, []), [], permutations);
  in permutations(msort(ls))
  end;

fun lexicographicPermDup(ls) =
  let fun present(ls, a) =
        if null(ls)
        then false
        else if hd(ls) = a
             then true
             else present(tl(ls), a);
      
      fun optimizedList(ls, r) =
        if null(ls)
        then r
        else optimizedList(tl(ls), if present(r, hd(ls)) then r else r @ [hd(ls)]);
  in optimizedList(lexicographicPerm(ls), [hd(lexicographicPerm(ls))])
  end;