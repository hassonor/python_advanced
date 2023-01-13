## Python_advanced and friends

#### Version Numbering

___
**PEP 440** introduces a version format that every Python package, and ideally every application, should follow so that
other programs and packages can easily and reliably identify which versions of your package they require.<br>
**PEP 440** defines the following regular expression format for version numbering:
```N[.N]+[{a|b|c|rc}N][.postN][.devN]```<br><br>
This allows for standard numbering such as 1.2 or 1.2.3 There are a few further details to note:

* Version 1.2 is equivalent to 1.2.0, 1.3.4 is equivalent to 1.3.4.0, and so forth.
* Versions matching `N[.N]+` are considered **final** releases.
* Final components can also use the following format:
    * `N[.N]+aN` (for example, `1.2a1`) denotes an alpha release; this is a version that might be unstable and missing
      features.
    * `N[.N]+bN` (for example `2.3.1b2`) denotes a beta release, a version that might be featured complete but still
      buggy.
    * `N[.N]+cN` or `N[.N]+rcN` (for example, `0.4rc1`) denotes a (release) candidate. This is a version that might be
      released as the final product unless significant bugs emerge. The `rc` and `c` suffixes have the same meaning, but
      if both are used, `rc` releases are considered newer that `c` releases.
      <br><br>
    * Many **_distributed version control system_** (DVCS) platforms, such a Git and Mercurial, are able to generate
      version numbers using an identifying hash (for Git, refer to `git describe`). Unfortunately, this system isn't
      compatible with the scheme defined by **PEP 440**: for one thing, identifying hashes aren't order-able.