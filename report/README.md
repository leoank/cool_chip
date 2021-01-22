# Report

## Getting started

### Requiremnts

- Latex distribution (MacTex, MikTex, TexLIve)

### Get Kaobook dependency

Create a tex dir in texmf home dir

```bash
kpsewhich -var-value=TEXMFHOME | cat | awk '{print $1"/tex"}'| xargs mkdir -p
```

Change directory

```bash
kpsewhich -var-value=TEXMFHOME | cat | awk '{print $1"/tex"}'| xargs cd
```

Clone Kaobook repo

```bash
git clone https://github.com/fmarotta/kaobook
```

### Build report

Create a `build` folder at the source of the repo

```bash
mkdir build
```

Use latexmk to build report

```bash
latexmk -synctex=1 -interaction=nonstopmode -f -outdir=build
```

Generated pdf will be at `build/main.pdf`
