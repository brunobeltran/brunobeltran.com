### What makes science...trustworthy?

And why? [Recent polls show](https://www.pewresearch.org/science/2019/08/02/trust-and-mistrust-in-americans-views-of-scientific-experts/)
that scientists are largely still trusted by the American public. However, dive
into conversation with anyone in the "mistrust" camp, and you'll quickly see
that the internet age has tragically (ironically) led to an erosion of trust in
science that would have been unfathomable to the generation that welcomed the
atomic age.

While this eroded trust has serious consequences societal consequences, very
rational people can be found at all points along the spectrum of trusting
science, suggesting that some of the mistrust should be taken seriously, as
legitimate complaints about the scientific community.

Scientists are not perfect creatures, and "bad" or "preliminary" scientific
results (such as animal trials of cancer drugs) are often sold to the public
under the same umbrella of "science" that we use to talk about well established
theory (such as Einstein's relativity). It is not surprising, then, that the
general public would develop frustration; it would be hard to not feel like
someone is trying to use the label of "science" to sell you dubious results.

[Many](https://journals.sagepub.com/doi/abs/10.1177/0093650214534967)
[different](https://www.pnas.org/content/111/Supplement_4/13664)
[people](https://royalsocietypublishing.org/doi/10.1098/rsos.181870) have
written about the need to communicate uncertainty in science effectively, but
humans are famously awful at understanding uncertainty.

We need a way of

You'd be hard-pressed to find a working scientist that doesn't have a personal
answer to this question. If they don't have it penned into words, they surely
have years of accumulated intuition that they can quickly use to decide whether
something is "good science", "bad science", or "not science at all" (depending
on how opinionated they are, they might even be willing to eschew the middle
category altogether!)

However, you'd be equally hard-pressed to find a conference or scientific forum
where two scientists aren't arguing about exactly whether a particular result
is or is not "good science". I have always felt that these conversations tend to
largely involve people talking right past each other. Sure, there are cases when
the entire room agrees that somebody has not done good science. However, it is
far more often the case that the real issue seems to be that different people
simply have different approaches to "science". After the references to
Popper and Hume are over, and the participants have stopped comparing their
personal scientific process to the development of the [Standard
Model](https://en.wikipedia.org/wiki/Standard_Model), it always seems that both
parties end up agreeing that everybody's approach is important (except for the
social scientists, they never get to be in the "in" group).

In this little blog-rant, I'd like to convince you that it's much more
productive to stop trying to define what "is" science and what "isn't", and
that it is not that hard to instead find a simple, shared language for the many
kinds of activities that currently fall under the umbrella of "science".

#### A Model of Models

It makes the most sense to start my diatribe against people who try to "define"
what science is with a definition of science:

+ *Science is a set of strategies we use to build predictive models about the
  world around us*

Hopefully this is a sufficiently abstract (read: useless) definition that nobody
can argue against it. It says nothing about what those strategies are, nor does
it even mention experimentation! However, "predictive model" is quite a loaded
word here, so it makes sense to unpack what is meant.

By "model", I tend to mean a mapping between observables and mathematical
objects. However, I don't mean that I require the "model" to be written down in
the conventional language of early 21st century mathematics, I merely want
whatever language is used to describe the observables to be unambiguous enough
to allow you to draw clear, logical conclusions about the observables. Some
examples:

1.  Kepler's "Law of Orbits": all planets move in elliptical orbits, with the
    sun at one focus.
  + The observable (distance to the sun) is mapped onto a mathematical object
    (the distance between an ellipse and one of its foci).
  + While not expressed in terms of algebraic equations, the language is
    sufficiently clear that you can draw unambiguous logical conclusions, like
    "the rate of change of the distance to the sun depends on both the speed
    around the ellipse and where on the ellipse we are".
2. The inverse square law of gravity: a much more classically "mathematical"
statement. Two objects $m_1$ and $m_2$ with positions $r_1$ and $r_2$ and masses
$M_1$ and $M_2$ will interact with a force of magnitude $GM_1M_2/|r_1 - r_2|^2$.
  + The choice of observables and mathematical objects here can be done with
    varying levels of sophistication, but as a simple case, we can take the
    observables to be the positions and velocities of any set of masses (defined
    as objects which we observe to travel as a unit when force is exerted on
    them) and the mathematical object is a set of differential equations in
    $\mathbb{R}^3$ describing their time-evolution due to a force that acts on
    $m_i$ as $\sum_{j\neq i} GM_iM_j(r_j - r_i)/|r_j - r_i|^3$.
  + By virtue of being a mathematical statement (a differential equation), the
    unambiguity of the logical conclusions of this mapping are clear.
3. Descriptive statements, e.g.: We have a sun.
  + The observable (existence of a sun) is trivially mapped onto the value
    "True" in some 2-tuple ("True", "False").
  + This technically allows us to draw only the "trivial" conclusion, which is
    the restatement of our observable. Nonetheless, this is the foundation upon
    which more complicated models (which include multiple observables as input
    and predict others as output) are built.
4. Diffusion of gas molecules at equilibrium: a particle of gas at a given
temperature will have a mean squared displacement proportional to the square
root of the time elapsed.
   + Here, properly mapping between a mathematical object (a random variable)
     that captures what is meant by the plain english statement and the gas
     particle's position requires some sophisitication, but it can be done.
   + In particular, I just wanted to point out that models need not be
     deterministic.

By "predictive", I mean something very subtle (because I don't believe in
"causality", more on that later, I promise I'm not crazy). For a model to be
"predictive", it merely needs to expresses a relationship between different
observable that we expect to *always be true*. For example:

1. Kepler's "Law of Orbits": once we determine two points on the ellipse, we can
   predict what all of the values that are observable ("distances from the sun")
   can take are.
2. Newtonian gravity: this is a parametric model, meaning it requires some
   measurement of our observable to fully specify (in this case, we need to take
   enough measurements of various bodies interacting gravitationally to measure
   $G$). After initial parameterization, the model is predictive, it can take
   any set of measured velocities and positions and (in theory) predict the
   positions and velocities of the masses for all of time.
   + **NOTICE**: I did not say "all time future time". We can just as well
     predict what the positions should have been in the past as we can predict
     what they were in the future. We may not be able to retroactively test this
     type of prediction (someone would have had to measure the past ahead of
     time, hide the values from us, then give them to us later to compare our
     predictions to), but it makes just as much sense to say that we've
     "predicted" the past as it does to say we've "predicted" the future.
3. Descriptive statements fail to be predictive. They do not link multiple
   observables, and so when interpreted as "models" they can only "predict"
   themselves.
4. Diffusion of gas molecules at equilibrium: a simple parametric model like
   Newton's laws above. The important thing to notice is that while the
   prediction is statistical, it is expected to hold exactly in probability
   (hence satisfying my "always true" requirement above).

I guess it makes sense to explicitly compare my definition of "prediction" with
the common usage of the word "counterfactuals" within the philosophy of science.
In my opinion, this is an unnecessarily supercilious word.
Basically, a model is predictive if it can take some information about how the
world is and predict some other information about the world.
Once one has a predictive model, predictions can be made based on actual
observations, or else the inputs to the model can be drawn some other way, in
which case the resulting prediction is called a counterfactual.

#### That's not science!

"But wait!", you might be screaming. "$X$ satisfies your definition, but I most
definitely would not call it science!"

I probably agree. But as I stated from the outset, I'm not in the business of
defining what science is and isn't. I'm much more interested in describing the
many things that people *call* science, so that we can have a language for
discussing their relative merits. And if $X$ satisfies my definition, I bet
there's at least one person out there right now trying to pass it off as
science.


<!-- version 2 -->

In a sentence: science is set of strategies for learning about the world around
us by studying the logical implications of various properties of the universe
that we believe to hold universally.

This phrasing probably sounds silly. After all, if my conversations with
scientists are at all representative, anyone reading this will probably either
feel that the definition misses some important facet of what they think of as
"science", or else just think that the definition is uselessly abstract.
However, I think that (modulo semantic issues about what exact parts of the
broader "scientific process" we choose to call science) I can convince any
scientist that not only is this definition useful, but that it contains all the
"magic bits": the special ingredients that make science useful and successful.

Being a contrarian at heart, I think it's the most fun to start with
some examples of things that *look* like science, but that this definition
excludes as being strictly *not* science.

#### Non-science #1: Statistics

> Say I am an intrepid young scientist, and having just learned about the
> "scientific method" in school, I am tasked with coming up with a science fair
> project. Since hypothetical me lives in the northeast United States, there are
> many abandoned buildings from the early 18th and 19th centuries. I have always
> wondered why the doorways and roofs seemed so short compared to those in my own

One of the most
When is fitting, let's say, a linear model, considered science? It's easiest to
see by example. When measuring the velocity of something falling on the moon, it
seems to make scientific sense to fit this (possibly noisy) data to a linear
model. This is because we have hundreds of years of data suggesting that an
approximately constant force of gravity will be the only real contributor to the
motion, and so we expect that if we measured everything more accurately
(decreasing the noise) that the linear model would continue to describe the data
well.

On the other hand, fitting estimates for the average height of all humans in
each year with a linear function seems less "scientific".  Even if the data
looks basically like a noise linear process, we do not expect at all that if we
measured more and more people (or more and more years in the past/future) that
the linear model would continue to perform well. For a model to be a "scientific
model", we must <em>reasonably expect</em>that the model will continue to work
as we collect more measurements.

Don't get me wrong, statistics is incredibly important to the scientific
process.
> Fits from statistical models can even be used as inputs (assumptions) for more
> scientific models (if we simply show that the consequences of the scientific
> model we care about don't depend strongly on the exactly output of the
> statistical model).
But the slope of a linear model that was fit to a cloud of data should not be
called a "scientific" finding. It is (merely) a statistical finding.


#### Non-science #2: Unverifiable models

Models that can only be distinguished from other models via predictions that can
not be verified in any way are not scientific.

This most famously includes string theory, but also encompasses as a special
case certain types of model selection that are normally relegated to Occam's
razor.  For example, when comparing between a model of gravity and a model where
gravity has identically the same properties but is generated by an unmeasurable
space fairy that orbits outside the milky way, the latter can be dismissed out
of hand as being unscientific. If we replace the space fairy with a massive
obelisk in low-earth orbit, now the latter theory is at least scientific (it is
testable) although it is true that heuristically, it makes sense to dismiss it
out of hand (this is Occam's razor), the reasons we dismiss it are totally
different, even if they seem similar.


#### Defining science by the "scientific method"

While (arguably) useful for teaching children about what doing science is like,
the scientific method is far enough removed from the everyday experience of
doing science that, as I near the end of my PhD, it seems comical to even write
it down.

1. Ask a question
2. Do background research
3. Construct a hypothesis
4. Test with an experiment
5. Analyze the data
    + if the results align with the hypothesis, you can't reject it
    + if the results *don't* align with the hypothesis, you can reject it!
6. Communicate your results (and have them replicated and vetted).

Most scientists will feel that this process does vaguely reflect the steps they
follow. Maybe it doesn't reflect their personal practice of science, but it
definitely does describe the outline of the story they have to tell at the end
of the day when drafting a paper or writing a grant.

What this definition lacks is any tool for describing the line that separates
exploratory statistical analysis and science. What, after all, is the difference
between what humans do when we look at the world around us and what a modern
machine learning algorithm does?

Modern ML has become much better than humans at uncovering hidden statistical
correlations between the various observations it makes of its surroundings.
However, the point of science is to identify which of these
correlations should be thought of

But what this description is missing is the most important part of the
scientific method: how to formulate a hypothesis for it to be scientific.

As implied by step 2 above, science is not done in a vacuum. There are many
scientific "facts" which we accept with various degrees of confidence.

#### Defining science by process

The process of science is often summarized by a simple loop:

1. Identify some property of the world around us that seems to be universally
   true.
2. Identify the logical consequences of that property.
3. Test for the logical consequences, and keep poking around until you're either
   unable to falsify your theory given your operating constraints or until
   you've found some inconsistency.
4. When an inconsistency is found, return to step 1 and identify the new
   universal property.
<!--
 -->
<!-- Of course, science often engages in some -->
<!-- seriously meta games. It might be that -->
<!-- instead of observing first some symmetry of -->
<!-- the universe, we instead first observe a -->
<!-- bunch of particles in our collider that -->
<!-- we know mathematically would emerge in the -->
<!-- case when there is some underlying symmetry -->
<!-- (which may actually predict many other -->
<!-- particles that we have not seen before). -->
<!-- This doesn't really follow the 4-step plan I -->
<!-- lay out above (even though it is obviously -->
<!-- an example of extremely good science). -->
<!-- However, it does follow the gestalt of the -->
<!-- above, in that it involves identifying a -->
<!-- specific set  of mathematical (i.e. -->
<!-- axiomatizable) "assumptions" whose logical -->
<!-- consequences can be directly tested. -->
<!--  -->
#### Defining science as "model-driven"


The cornerstone of the process described above is what I'd call the "successful,
falsifiable model".

+ By <em>"model"</em>, I mean a mathematical description of some process that
  generates observations of the world around us. (Where mathematical simply
  means it is unambiguous, and has unambiguous logical consequences).
+ By <em>"successful"</em>, I mean that we can be reasonably confident that the
  model will remain accurate upon continued testing.
+ Finally, by <em>"falsifiable"</em>, I mean that every "assumption" of the
  model can in principle be tested.


You might notice in particular that I've punted hundreds of years of philosophy
of science into the catch-all phrase: "reasonably confident".  This is not
because I don't understand the complexity involved in trying to specify exactly
what are the properties that should make one "reasonably confident" that a model
will remain accurate upon adding further measurements. Rather, it is exactly
because I admit that I personally believe that "good" science (as currently
practiced) is basically just a huge grab bag of heuristics for what kinds of
models are useful (e.g.  those that have stood the test of time and repeated
verification, those that are as simple as possible, those that rely on the
fewest unmeasured parameters, etc). And while I think these are important for
doing "good" science, in practice, they are ignored by working scientists as
needed to accomplish their particular goals.

In particular, notice that I don't include any notion of the "simplicity" of the
model in my definition of science. That is in fact because I actively do not
think that science is necessarily about the pursuit of the "simplest possible"
model of a system. In fact, I tend to actually <a
href="#blog.physics-vs-biology">define physics</a> as the subset of science
whose sole purpose is to generate the most simple model of a system possible
given existing data.

#### Defining science as leveraging logic to facilitate the search for truth

Science turns out to be a word which is used to describe quite a diverse range
of activities that are undertaken in the search of knowledge.
1. (exploratory experimentation and hypothesis development) Broadly, searching
   for underlying universal properties of the world around us by looking for
    patterns in observations.
2. (theoretical development) Developing the logical consequences of existing
   ("known") patterns in the world around us.
3. (experimental verification and falsification) "known" consequences of "known"
   patterns in the world around us to look for discrepancies, since these will
   stem (in a real model) from incorrect assumptions that should be revised.

> By "universal properties" above, I don't necessarily mean "fundamental" or
> "simplest", just "reproducible". Even without a complete understanding of
> epigenetics, we were able to map out how gene expression works for some easy
> bacterial genes early on (e.g. the <i>lac</i> operon). The principle that a
> transcription factor needs to be chemically modified by the environment and bind
> to the promoter was not a "universal" or "fundamental" description of how gene
> expression works, but it was the best description that we had (and agreed with
> all data available at the level of coarse-graining that was required by models
> of the time).

However, if we simply go around calling everything that seems to fit in this
extremely broad framework by the name "science", we will find that it does not
distinguish very well between well-respected theories and total quack science.

#### Things that are science

Many theoreticians would probably take offense to my requirement that scientific
models need to be expected to be able to reproduce experimental data arbitrarily
well. After all, many models (my entire scientific career included) are
considered worthwhile not because they can reproduce experimental measurements.
For example, a very popular approach widely known as "bottom-up" modeling
totally eschews attempting to match any data at all.  Instead, bottom-up
modeling takes small subset of only the most well-accepted facts about a complex
system and tries to derive the consequences of only that subset of properties.
By doing so, the modeling process is made infinitely more tractable, and the
individual effects from the different parts of the system can often be teased
apart much more easily. However, this of course comes at the cost of being able
to reproduce data.

#### Assumption complexity: a useful classifier for "types" of science

I find that one of the most useful metrics by which to classify scientific
models is by how detailed the assumptions need to be in order to produce the
model's logical conclusions (given our current understanding of mathematics).

On one extreme, you'll tend to find models that come out of very applied fields
such as biology or materials science. Say you are interested in the science
behind how a microbe works. It's entirely possible that in order to develop a
model that faithfully reproduces every facet of such a complicated entity, you
need to basically plug in so many details (assumptions) about the microbe in
question that you begin to ask yourself if you're actually learning anything or
just carefully reverse-engineering. These models gain their utility from being
able to explain specific systems that affect humans here and now.

On the other extreme, you'll tend to find models from more "theoretical" fields
such as physics or computer science.  Practitioners of these fields will tend to
specifically be interested in what logical conclusions can be drawn from small
sets of assumptions. For example, a physicist might ask what assumptions can be
drawn about the electromagnetic force assuming a particular type of symmetry
(locally U(1)) that it has been observed to obey. These models will contain a
very small set of assumptions and as provide utility by being broadly applicable
to a wide range of problems.

Both types (and everything in between) are useful. Both types are science.

Are there things which are "not" science? Definitely.

<!-- first version -->


Any attempts to build a falsifiable model that describes observations about the
world around us is science, as is the testing of such a model, as is the
exploration of potentially unexplored types of measurements about the world with
the purpose of building a model. At least that's a tempting thing to say, and
maybe it summarizes the most well-accepted bits of the "philosophy of science",
from Bacon, to Popper to Hempel.
<!-- However, I often see this definition -->
<!-- being used as a sort of checklist, by people -->
<!-- that want to do "science", but somehow end -->
<!-- up doing bad stats on ugly data. -->


<strong>BUT</strong>, I think that almost any modern scientist, if forced to,
could do a much better job at describing what is meant at the turn of the 21st
century by "good" science than this simple description.
<!-- It's easy to do better than centuries of -->
<!-- brilliant philosophers at describing -->
<!-- something that you have centuries more -->
<!-- examples of, but we're going to do it -->
<!-- anyway. -->

First, what is so bad about the previous definition? When used as a checklist,
it allows one to call a lot of things science that a working scientist would
take great offense to. For example, say I measure a bunch of people's heights
over the last few decades. Now I fit a line to their heights as a function of
time. I claim that people's heights are growing at an average rate given by the
parameter of my model fit. The number of ways in which this is "hardly" science
are almost too numerous for any working scientist to point out, but it seems to
check all of the boxes! There's a model (albeit an unmotivated, oversimplified,
seemingly arbitrary one). It's falsifiable (more measurements, or maybe
measurements in the future or past could show that this trend no longer holds or
never held at all).  My measurements might have been the first of their kind, I
might have predicted height would increase on average over time <i>a priori</i>,
and still no scientist worth their salt would call what I did science.  Maybe if
confronted with a definition of science like the one above, they would cave and
just mutter that it's not "good" science in any case. Many of the less
politically correct...physicists...in the room would even be likely to mutter
that "this might pass for real work in the social sciences, but not in [my]
department."

Now I don't agree with my colleagues that think that social sciences are
"lesser" than the "hard" sciences, but the things they are recoiling at stem
from a shared understanding of what types of science are useful, what types of
scientific questions tend to be fruitful, and what types of approaches tend to
most often lead to bogus results. The above example really does go against
dozens of unspoken "rules" about what is allowed to be called science within the
community. They recoil because such a seemingly useless piece of work flows
directly against the zeitgeist of early 21st century science, and this zeitgeist
exists for a reason.

Well, the obvious follow-up question is: can we amend our previous definition of
science to more completely contain this shared understanding of what constitutes
"real" science, as opposed to things that simply masquerade as scientific? Of
course, as someone whose graduate "schooling" was largely <a
href="#blog.physics-vs-biology"> guided by physicists</a>, it is my solemn duty
to believe that not only can I summarize this complex set of rules, but that I
can do so in a manner that distills them into a much simpler set of underlying
principles that should drive how everybody does science.

Jokes aside, dozens of much smarter people than me have tried this same exercise
over the centuries since humans have left behind writings about science.
However, like a middle schooler solving algebraic equations that only
specialized mathematicians would have been acquainted with in ancient times, I
have the advantage of modernity: everything is much easier in hindsight.

In order to better define what science is, we're going to sketch out a model for
how an abstract (set of) agent(s) might go about discovering things about the
world around themselves. I don't intend to provide a rigorous definition or
example of such a model, but merely to point out the types of strategies that
might emerge, so that I can more precisely specify which of these I would call
"science".

So if you want a model describing a set of agents trying to discover the
universe around them, you need to specify something about the universe that
you're talking about. And if you want to say things about how universally
applicable their strategy is, you need to in fact describe the sets of universes
over which you want to gauge their potential for success.

This may seem like a silly proposition, but I'd argue that we can quickly list
off various properties of universes that are necessary for the question we're
asking to even make sense in the first place.

1. The universe better be complex enough that it can support (as in it can
   contain) agents that can ask questions about the universe.
2. On the time scales on which these agents ask their question, the universe
   better have at least reasonably constant underlying rules.

The complexity lower-bound means that the universes we're talking about have to
at least admit Turing-complete machines.  The other property is mostly just to
simplify the questions that we're asking.  And while there are <a
href="https://en.wikipedia.org/wiki/Time-variation_of_fundamental_constants">
valid reasons to ask if the laws of physics as-currently-written describe rules
about our own universe that are actually "unchanging"</a>, the majority of the
scientific community can safely assume that the fundamental laws of physics are
unchanging (hence the "reasonably" above).

For our model of the "scientific" process, we will consider a observable
universe, a set of existing observations, and a set of (possibly evolving)
methods for generating new observations. A "knowledge set" contains a set of
patterns that have been observed to hold (exactly, statistically, or otherwise)
in the existing observations.

We define "reason" to be the set of rules by which the elements of the
"knowledge set" are assigned "confidences". And we define "science" to be the
process by which new patterns in existing observations are searched for
(hypothesis development), their consequences are enumerated (theoretical
development, i.e. mathematics), and new measurements are chosen with which to
attempt to verify or falsify existing hypotheses.

Is reason just really fancy statistical pattern-matching with some kind of
power-law memory decay? Yeah probably.

In this framework, some "good" types of science are:


+ Finding
+ Finding consequences of high-confidence hypotheses that directly contradict
  low-consequence hypotheses, and removing the contradictory low-confidence
  hypothesis.
+ Finding consequences of high-confidence hypotheses that are also in our
  knowledge set. Patterns in our knowledge set that are





