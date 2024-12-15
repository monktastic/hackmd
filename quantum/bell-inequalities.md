# Bell's Inequalities for Dummies

Imagine you have a large collection of items, each defined by three binary properties called A, B, and C. Each property can be either 0 or 1, meaning there are eight possible combinations in total. For example, one item might have A=0, B=0, C=1, while another might have A=1, B=1, C=0.

Now suppose you count the total number of items where A=0 and B=0, regardless of the value of C. Let’s denote this quantity as N(0, 0, x), where x means “don’t care.” A simple inequality that can be proven is:

N(0, 0, x) ≤ N(x, 0, 0) + N(0, x, 1)

Why does this hold? It follows from two basic observations:

- N(0, 0, 0) ≤ N(x, 0, 0), because N(x, 0, 0) includes all items where B=0 and C=0, whether A=0 or A=1.
- N(0, 0, 1) ≤ N(0, x, 1), because N(0, x, 1) includes all items where A=0 and C=1, whether B=0 or B=1.

Adding these two gives us the original inequality.

Now imagine you can’t directly count all the items in your collection. Instead, you draw one item at a time through a random process, and for each item, you can run one of three tests. Each test measures two of the three properties, ignoring the third. For instance:

- One test may measure A and B, contributing to your estimate of N(0, 0, x).
- Similarly, two other tests can help you estimate N(x, 0, 0) and N(0, x, 1).

If you repeat this process enough times, the inequality should hold in the long run.

## Introducing Entanglement

Now let’s add a twist. Instead of directly feeding you the item that it draws, the process first "copies" it somehow, so that we get two identical copies. The details of this "copying" process remain obscure. Suppose all we know is that measuring the same property on each copy always yields the same result for both. This might be because the original particle came equipped with "internal instructions" that get copied to its partner, indicating what response to give to which measurement — possibly even at _which times_, if we allow for properties to change (as we soon shall). Alternatively, the two particles might be provided with some kind of signaling mechanism that keeps them in sync. Again, all we know from the outside is that they produce the same result for the same measurement.

These particles are then sent to two distant measuring stations. Each station measures one property (say, A for one particle and B for the other). The results from these measurements are then tallied as if they were measurements on a single item. We haven't changed anything substantial about the measuring process, so inequality should still hold.

Now for the crux: _what if experiments show that the inequality does not hold?_ Then one of our assumptions must be false. Namely, either:

1. The random process is not random. It somehow “knows” which tests we will run, and chooses tailored items to thwart our estimates. In other words, it introduces a persistent sampling bias that depends on what will be measured.
2. The particles do not have fixed values for A, B, and C. They're somehow adapting themselves to our tests in real time.

### Exploring case 2

Even if the particles randomly change their values in a coordinated way, the inequality will not break. After all, changing their properties in sync is equivalent to just having picked a different original item in the first place — and no matter which items we pick, so long as they are random, the inequality will hold in the long run. To help see why, let's revisit our inequality:

N(0, 0, x) ≤ N(x, 0, 0) + N(0, x, 1)

This only depends on the fact that if an item would pass the test on the left, then it would necessarily have passed one of the tests on the right. As long as the three properties are static, this must be true. But if they are allowed to "squirm around" _in the midst of conducting these three tests_, then nothing forces this logic to hold. In particular, if the remaining two properties can somehow change after the first has been measured, then our inequality can break. For this to happen in our scenario, the second particle would have to "know" that the first particle has been measured.

But here’s the catch: the two measurements are happening at a great distance from each other and nearly simultaneously. For the second particle to adjust its property in response to the first, information would have to travel faster than the speed of light—a violation of the principle of locality.

Einstein, in the famous [1935 EPR paper](https://cds.cern.ch/record/405662/files/PhysRev.47.777.pdf), realized that quantum mechanics implied this kind of seemingly faster-than-light “signaling.” Either that, or particles don't have well-defined properties prior to measurement. He could not countenance either possibility, so his attempted conclusion was that particles must have hidden variables — some unseen properties determining their behavior — that quantum mechanics doesn’t account for. This would preserve both realism (the idea that properties have definite values) and locality (the idea that nothing travels faster than light) — or so he thought.

## Bell’s Contribution

In 1964, John Bell proposed a way to test whether such hidden variables exist. He showed that any “local realist” hidden variable theory—where properties are well-defined and information doesn’t travel faster than light—must satisfy certain inequalities. Experiments by Alain Aspect and others in the 1980s tested Bell’s inequalities and found they were violated. In 2022, Aspect and two others received the Nobel Prize for their groundbreaking work.

The experiments typically involve properties like the spin or polarization of particles, measured at various angles. These are examples of non-commuting observables in quantum mechanics—quantities that cannot have well-defined values simultaneously under quantum rules. Until Bell’s work, it wasn’t clear whether quantum mechanics’ predictions about such observables could be reconciled with classical intuition.

## The Modern View

The modern conclusion is that no local realist hidden variable theory can fully explain the observed violations of Bell’s inequalities. “Local” means that information cannot propagate faster than light, and “realist” means that properties have definite values prior to measurement. To reconcile the experimental results, one of these principles must be abandoned.

The prevailing interpretation is that realism must go. While measuring one particle does seem to influence its entangled partner, no usable information is transmitted faster than light, so locality is preserved. Over the decades, further experiments and “no-go” theorems have closed potential loopholes in Bell’s argument, solidifying the conclusion that the classical idea of “reality” must be rethought.
