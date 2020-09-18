(TeX-add-style-hook
 "main"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "chapters/4-ksp/table"
    "chapters/4-ksp/02_intro"
    "chapters/4-ksp/03_relatedworks"
    "chapters/4-ksp/04_methods"
    "chapters/4-ksp/05_experiments"
    "chapters/4-ksp/06_conclusion"
    "chapters/4-ksp/07_appendix")
   (TeX-add-symbols
    '("blue" 1)
    '("red" 1)
    '("DLnb" 0)
    '("GSnb" 0)
    '("PSVMnb" 0)
    '("EELnb" 0)
    '("DL" 0)
    '("GS" 0)
    '("PSVM" 0)
    '("EEL" 0)
    '("KSPOPTnb" 0)
    '("KSPnb" 0)
    '("KSPOPT" 0)
    '("KSP" 0)
    '("comment" 1)
    '("mycommfont" 1)
    "fatline"
    "slimline"
    "eg"
    "ie"))
 :latex)

