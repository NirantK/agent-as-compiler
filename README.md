# The Agent as Compiler

A conference talk by Nirant Kasliwal (Scaled Focus) on harness engineering. The
argument: a coding agent is a compiler. The model weights are a swappable middle
IR, and the harness, the ordinary code in Python, Rust, and bash around the model,
is the backend that does the real work.

`agent-as-compiler.html` is a single, self-contained deck. Every font, image, and
video is embedded, so it has zero external dependencies. Open it in any browser and
use the arrow keys or space to move between slides.

## Build

Act II and Act III live in `act2-loopcraft/index.html`. The Act I slides and the
asset embedding live in `build.py`:

```
python3 build.py
```

That inlines every asset as base64 and writes `agent-as-compiler.html`.

## The three acts

1. The harness was always the work. The model is the cheap part.
2. Coding agents are compilers. Stack loops, build the verifier, generate the harness.
3. Reward is all you need. Own the loop, don't rent the model.

## Credits

- Loopcraft diagram and quote: swyx, latent.space
- Demo clip: @anshuc, running GLM-5.2
- Law of requisite variety: W. Ross Ashby, *An Introduction to Cybernetics*, 1956
- References: Universal Geometry of Embeddings (arXiv:2505.12540), auto-harness
  synthesis (arXiv:2603.03329), Meta Harness (yoonholee.com/meta-harness)
- Opening photo: Wingify DevFest 2018
