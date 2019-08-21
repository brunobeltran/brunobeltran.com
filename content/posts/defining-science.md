### What is science?

Science, at the end of the day, is really just the process by which we map our
observations of reality onto the world of mathematics (the persnickety
philosopher can find an [incoherent rant](#trusting-science) with more details
about what I mean [here](#trusting-science)):

![Flowchart: a scientific theory is simply a map from observational data
(\\(d\_i\\)) to a set of mathematical objects
(\\(X\_i\\))](./images/observations-to-math.svg)

As long as we're living completely on the right side of this diagram (in the
world of mathematics) it makes sense to say that "assumptions A, B, and C
**prove** conclusion X". As long as you specify A, B, and C well enough, either
"\\(A+B+C \Rightarrow X\\)"or it doesn't. There is no way for someone to disagree
with a valid proof that "\\(A+B+C \Rightarrow X\\)". Sure, anyone can misunderstand
a complicated enough mathematical statement, but anyone that continues to
disagreee with valid logic once it's been made clear doesn't deserve to be part
of the conversation.

On the other hand, scientific statements tend to be more complicated creatures.
Often, they take the form of predictions about new data made using existing
data:

![Diagram: a theorem like \\(X\_1 \implies X\_2\\), and a scientific theory
that associates \\(X\_1 \to d\_\text{existing}\\) and \\(X\_2 \to d\_\text{new}\\)
leads to a scientific claim that \\(d\_\text{existing} \implies
d\_\text{new}\\)](./images/scientific-claim-diagram.svg)

Suddenly, there are several levels on which you can disagree with someone. Let's
take a concrete example. Say my physical theory is just Newton's gravity
(\\(T\_i\\)), and suppose you have some set of measurements, like the initial
trajectory of a satellite that you've launched (\\(d\_\text{existing}\\)). If I
say to you, "given this initial trajectory, the satellite's orbit will be
so-and-so (\\(d\_\text{new}\\)) in two days", there are several ways you can
disagree with that statement:

1. You can disagree with the mathematical content of my claim (i.e. if I messed
   up my calculations, then \\(X\_1 \nRightarrow X\_2\\))
2. You can disagree with the accuracy of the initial set of measurements, in
   which case my calculations could be right but I'd still be wrong (i.e. you
   reject \\(d\_\text{existing}\\))
3. You can disagree with my choice of model (i.e. you reject \\(T\_i\\)). And in
   this case, you'd probably be right, since relativistic effects are likely not
   negligible in this case, we should probably use Einstein's theory
   (\\(T\_{i+1}\\)) instead)

On the other hand, if you accept \\(d\_\text{existing}\\), you accept that
\\(X\_1 \nRightarrow X\_2\\), and you believe that the physical theory
\\(T\_i\\) should hold, then you must agree with my conclusions.

**Science is the process by which we select increasingly accurate scientific
models.**

And this process is entirely based on [heuristics](#science-heuristics).


