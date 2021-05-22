# Sailfish OS RPM Spec for Argon2

This RPM spec file is for compiling `libargon2` and `libargon2-devel` for
Sailfish OS and specifically for the `aarch64` architecture. (It has only been
tested on `aarch64`.)

This library is a build and run dependency for
[ownKeepass](https://openrepos.net/content/jobe/ownkeepass) for which the
official repository at the moment only has `i486` and `armv7hl` packages.

This is my first RPM spec file ever, so feel free to point out improvements.

## Dependencies

### Build

- [Sailfish OS Builds in Docker](https://git.sr.ht/~aerique/sfosbid)

## Build Steps

### Preparing Sailfish OS Builds in Docker

- `mkdir ~/software` (if it does not exist yet)
- `cd ~/software`
- `git clone https://git.sr.ht/~aerique/sfosbid sfosbid-git`
- `cd sfosbid-git`
- `./download.sh`
- `./build.sh -u`
- `./run.sh -u`

### Building libargon2 and libargon2-devel

This section assumes you've run `./run.sh -u` from the previous section and are
now in the Docker container.

- `cd projects`
- `git clone https://git.sr.ht/~aerique/libargon2-spec libargon2-spec-git`
- `cd libargon2-spec-git`
- `git submodule update --init --recursive`
- in `argon2/qmake/libargon2/libargon2.pro` change `target.path` from `/usr/lib`
  to `/usr/lib64`
- `mb2 -t SailfishOS-latest-aarch64 build`

If the build finishes successfully you'll now have `libargon2` and
`libargon2-devel` packages in the `RPMS` directory.  These will also be
available outside of the Docker container if you leave it.
