datatype LEXP = APP of LEXP * LEXP | LAM of string * LEXP | ID of string;

fun printLEXP (ID v) = print v;
  | printLEXP (LAM (v, e)) = (print "(\\"; print v; print "."; printLEXP e; print ")");
  | printLEXP (APP (e1, e2)) = (print "("; printLEXP e1; print " "; printLEXP e2; print ")");

(* Define the term λ xz.xz *)
val vx = ID "x";
val vz = ID "z";
val t101 = LAM ("x", LAM ("z", APP (vx, vz)));

(* Call the print function to display the term *)
printLEXP t101;
