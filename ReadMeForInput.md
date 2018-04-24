Inputs can be taken in NASM.
Below, All the examples used during evaluation in the project are shown.
The result file will be shown in Output.txt

NASM 

1.Conditional Macro not previously defined.
  ----------------------------------------
Input
-----

%ex? MAX	
    a=10
    b=20
%/ex?

Output
------

2.Conditional Macro previously defined.
  ------------------------------------
Input
-----

%expand MAX 5

%ex? MAX
    a=10
    b=20
%/ex?

Output
------

    a=10
    b=20
   
   
2. Functional 

Input
-----

%expand SQU(x) ((x)*x)
x=SQU(3)

Output
------
x=((3)*3)

3. Functional Multiple Arguments
Input
-----

%expand ADD(a,b) s = a + b
ADD(3,4)

Output
------

s = 3 + 4

4. Multiline
Input
-----

%expand lol \
\
   print "this is statement 1"\
   print "this is statement 2"\

lol

Output
------



    print "this is statement 1"
    print "this is statement 2"

5. Nested
Input
-----

%expand SQU(x) ((x)*x)
%expand CUBE(x) (SQU(x)*x)
a=CUBE(4)

Output
------

a=(((4)*4)*4)

6. Single line 
Input
-----

%expand MAX 5
t=MAX

Output
------
t=5





	






	




