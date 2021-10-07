# Homecomputer Fonts (Sixtyfour)

Variable fonts based on the Commodore 64 fonts.

Inspired by the article [Raster CRT Typography (According to DEC)](https://www.masswerk.at/nowgobang/2019/dec-crt-typography) by Norbert Landsteiner, I reworked some old pixel versions of the [Commodore 64](https://github.com/jenskutilek/homecomputer-fonts) and [Amiga Workbench fonts](https://github.com/jenskutilek/homecomputer-fonts-wb) I had done years ago to include variable font axes for the size of the horizontal scanlines and the amount of horizontal bleed of the pixels due to the phosphor latency found in CRT displays.

<figure>
	<img src="documentation/images/64.png">
	<figcaption>Sixtyfour, check the <a href="https://jenskutilek.github.io/homecomputer-fonts/demo-sixtyfour.html">interactive demo page</a>.</figcaption>
</figure>


# Building the fonts from source

To use `gftools builder`, I had to [jump through some hoops](https://www.pygit2.org/install.html#libgit2-within-a-virtual-environment) to install pygit2 on macOS.

Activate the virtual environment:

```bash
source env/bin/activate
```

When you have got it, you can just type

```bash
make build
make test
make proof
```
