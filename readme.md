Houdini 存檔時選擇 `Save As Text`，然後將存成的 hip 檔案解析產生資料結構並餵给 git 來管理。

git 更動範例: https://github.com/elishahung/houdini-git-structure/commit/335c534d429982b016fd98d4dc7cbcb10a302264
可以更好看見參數變更，節點關係改動，去做更好的版本控制。

資料生成結構範例
```
│  .aliases
│  .application
│  .contextoptions
│  .cwd
│  .hou.session
│  .OPdummydefs
│  .OPfallbacks
│  .OPlibraries
│  .OPpreferences
│  .scenefilevisualizers
│  .start
│  .styles
│  .takeconfig
│  .takes
│  .variables
│  ch.def
│  ch.net
│  ch.parm
│  ch.userdata
│  expression.func
│  img.def
│  img.net
│  img.parm
│  img.userdata
│  mat.def
│  mat.net
│  mat.order
│  mat.parm
│  mat.userdata
│  obj.def
│  obj.net
│  obj.order
│  obj.parm
│  obj.userdata
│  out.def
│  out.net
│  out.order
│  out.parm
│  out.userdata
│  shop.def
│  shop.net
│  shop.parm
│  shop.userdata
│  stage.datablocks
│  stage.def
│  stage.net
│  stage.parm
│  stage.userdata
│  tasks.def
│  tasks.net
│  tasks.parm
│  tasks.userdata
│  vex.def
│  vex.net
│  vex.parm
│  vex.userdata
│
├─img
│      comp1.def
│      comp1.init
│      comp1.net
│      comp1.parm
│      comp1.userdata
│
├─mat
│  │  constant.chn
│  │  constant.def
│  │  constant.init
│  │  constant.net
│  │  constant.order
│  │  constant.parm
│  │  constant.spareparmdef
│  │  constant.userdata
│  │  principledshader.chn
│  │  principledshader.def
│  │  principledshader.init
│  │  principledshader.parm
│  │  principledshader.userdata
│  │
│  └─constant
│      │  Alpha.def
│      │  Alpha.init
│      │  Alpha.parm
│      │  Alpha.userdata
│      │  Cd1.def
│      │  Cd1.init
│      │  Cd1.parm
│      │  Cd1.userdata
│      │  Ce.def
│      │  Ce.init
│      │  Ce.parm
│      │  Ce.userdata
│      │  chooseAlpha.def
│      │  chooseAlpha.init
│      │  chooseAlpha.parm
│      │  chooseAlpha.userdata
│      │  collect1.def
│      │  collect1.init
│      │  collect1.parm
│      │  collect1.userdata
│      │  difclr.def
│      │  difclr.init
│      │  difclr.parm
│      │  difclr.userdata
│      │  map.def
│      │  map.init
│      │  map.parm
│      │  map.userdata
│      │  map3.def
│      │  map3.init
│      │  map3.parm
│      │  map3.userdata
│      │  multiply1.def
│      │  multiply1.init
│      │  multiply1.parm
│      │  multiply1.userdata
│      │  multiply3.def
│      │  multiply3.init
│      │  multiply3.parm
│      │  multiply3.userdata
│      │  opacity.def
│      │  opacity.init
│      │  opacity.parm
│      │  opacity.userdata
│      │  output1.def
│      │  output1.init
│      │  output1.parm
│      │  output1.userdata
│      │  premultColors.def
│      │  premultColors.init
│      │  premultColors.parm
│      │  premultColors.userdata
│      │  texture1.def
│      │  texture1.init
│      │  texture1.parm
│      │  texture1.userdata
│      │  texture2.def
│      │  texture2.init
│      │  texture2.parm
│      │  texture2.userdata
│      │  twoway2.def
│      │  twoway2.init
│      │  twoway2.parm
│      │  twoway2.userdata
│      │  usePointAlpha.def
│      │  usePointAlpha.init
│      │  usePointAlpha.parm
│      │  usePointAlpha.userdata
│      │  usePointColor1.def
│      │  usePointColor1.init
│      │  usePointColor1.parm
│      │  usePointColor1.userdata
│      │  uvcoords2.def
│      │  uvcoords2.init
│      │  uvcoords2.net
│      │  uvcoords2.order
│      │  uvcoords2.parm
│      │  uvcoords2.userdata
│      │  vectohvec4.def
│      │  vectohvec4.init
│      │  vectohvec4.parm
│      │  vectohvec4.userdata
│      │
│      └─uvcoords2
│              choose_S.def
│              choose_S.init
│              choose_S.parm
│              choose_S.userdata
│              choose_T.def
│              choose_T.init
│              choose_T.parm
│              choose_T.userdata
│              float2vec.def
│              float2vec.init
│              float2vec.parm
│              float2vec.userdata
│              shadingAttriUV.def
│              shadingAttriUV.init
│              shadingAttriUV.parm
│              shadingAttriUV.userdata
│              subinput1.def
│              subinput1.init
│              subinput1.parm
│              subinput1.userdata
│              suboutput1.def
│              suboutput1.init
│              suboutput1.parm
│              suboutput1.userdata
│              s_global.def
│              s_global.init
│              s_global.parm
│              s_global.userdata
│              t_global.def
│              t_global.init
│              t_global.parm
│              t_global.userdata
│              vec2float.def
│              vec2float.init
│              vec2float.parm
│              vec2float.userdata
│
├─obj
│  │  source.def
│  │  source.init
│  │  source.net
│  │  source.order
│  │  source.parm
│  │  source.spareparmdef
│  │  source.userdata
│  │  to_bake.def
│  │  to_bake.init
│  │  to_bake.net
│  │  to_bake.parm
│  │  to_bake.spareparmdef
│  │  to_bake.userdata
│  │  __source.def
│  │  __source.init
│  │  __source.net
│  │  __source.parm
│  │  __source.spareparmdef
│  │  __source.userdata
│  │  __target.def
│  │  __target.init
│  │  __target.net
│  │  __target.parm
│  │  __target.spareparmdef
│  │  __target.userdata
│  │
│  ├─source
│  │  │  alembic1.chn
│  │  │  alembic1.def
│  │  │  alembic1.init
│  │  │  alembic1.parm
│  │  │  alembic1.userdata
│  │  │  autouv1.def
│  │  │  autouv1.init
│  │  │  autouv1.parm
│  │  │  autouv1.userdata
│  │  │  material1.def
│  │  │  material1.init
│  │  │  material1.parm
│  │  │  material1.userdata
│  │  │  material2.def
│  │  │  material2.init
│  │  │  material2.parm
│  │  │  material2.userdata
│  │  │  object_merge1.def
│  │  │  object_merge1.init
│  │  │  object_merge1.parm
│  │  │  object_merge1.userdata
│  │  │  raw.def
│  │  │  raw.init
│  │  │  raw.parm
│  │  │  raw.userdata
│  │  │  subnet1.def
│  │  │  subnet1.init
│  │  │  subnet1.inp
│  │  │  subnet1.net
│  │  │  subnet1.order
│  │  │  subnet1.parm
│  │  │  subnet1.userdata
│  │  │  uvlayout1.def
│  │  │  uvlayout1.init
│  │  │  uvlayout1.parm
│  │  │  uvlayout1.userdata
│  │  │  uvunwrap1.def
│  │  │  uvunwrap1.init
│  │  │  uvunwrap1.parm
│  │  │  uvunwrap1.userdata
│  │  │
│  │  └─subnet1
│  │      │  material1.def
│  │      │  material1.init
│  │      │  material1.parm
│  │      │  material1.userdata
│  │      │  matnet.def
│  │      │  matnet.init
│  │      │  matnet.net
│  │      │  matnet.parm
│  │      │  matnet.userdata
│  │      │  OUT_geo.chn
│  │      │  OUT_geo.def
│  │      │  OUT_geo.init
│  │      │  OUT_geo.parm
│  │      │  OUT_geo.userdata
│  │      │  OUT_preview_baked_source.def
│  │      │  OUT_preview_baked_source.init
│  │      │  OUT_preview_baked_source.parm
│  │      │  OUT_preview_baked_source.userdata
│  │      │  OUT_source.def
│  │      │  OUT_source.init
│  │      │  OUT_source.parm
│  │      │  OUT_source.userdata
│  │      │  OUT_target.def
│  │      │  OUT_target.init
│  │      │  OUT_target.parm
│  │      │  OUT_target.userdata
│  │      │  ropnet.def
│  │      │  ropnet.init
│  │      │  ropnet.net
│  │      │  ropnet.parm
│  │      │  ropnet.userdata
│  │      │
│  │      ├─matnet
│  │      │  │  constant.chn
│  │      │  │  constant.def
│  │      │  │  constant.init
│  │      │  │  constant.net
│  │      │  │  constant.order
│  │      │  │  constant.parm
│  │      │  │  constant.spareparmdef
│  │      │  │  constant.userdata
│  │      │  │
│  │      │  └─constant
│  │      │      │  Alpha.def
│  │      │      │  Alpha.init
│  │      │      │  Alpha.parm
│  │      │      │  Alpha.userdata
│  │      │      │  Cd1.def
│  │      │      │  Cd1.init
│  │      │      │  Cd1.parm
│  │      │      │  Cd1.userdata
│  │      │      │  Ce.def
│  │      │      │  Ce.init
│  │      │      │  Ce.parm
│  │      │      │  Ce.userdata
│  │      │      │  chooseAlpha.def
│  │      │      │  chooseAlpha.init
│  │      │      │  chooseAlpha.parm
│  │      │      │  chooseAlpha.userdata
│  │      │      │  collect1.def
│  │      │      │  collect1.init
│  │      │      │  collect1.parm
│  │      │      │  collect1.userdata
│  │      │      │  difclr.def
│  │      │      │  difclr.init
│  │      │      │  difclr.parm
│  │      │      │  difclr.userdata
│  │      │      │  map.def
│  │      │      │  map.init
│  │      │      │  map.parm
│  │      │      │  map.userdata
│  │      │      │  map3.def
│  │      │      │  map3.init
│  │      │      │  map3.parm
│  │      │      │  map3.userdata
│  │      │      │  multiply1.def
│  │      │      │  multiply1.init
│  │      │      │  multiply1.parm
│  │      │      │  multiply1.userdata
│  │      │      │  multiply3.def
│  │      │      │  multiply3.init
│  │      │      │  multiply3.parm
│  │      │      │  multiply3.userdata
│  │      │      │  opacity.def
│  │      │      │  opacity.init
│  │      │      │  opacity.parm
│  │      │      │  opacity.userdata
│  │      │      │  output1.def
│  │      │      │  output1.init
│  │      │      │  output1.parm
│  │      │      │  output1.userdata
│  │      │      │  premultColors.def
│  │      │      │  premultColors.init
│  │      │      │  premultColors.parm
│  │      │      │  premultColors.userdata
│  │      │      │  texture1.def
│  │      │      │  texture1.init
│  │      │      │  texture1.parm
│  │      │      │  texture1.userdata
│  │      │      │  texture2.def
│  │      │      │  texture2.init
│  │      │      │  texture2.parm
│  │      │      │  texture2.userdata
│  │      │      │  twoway2.def
│  │      │      │  twoway2.init
│  │      │      │  twoway2.parm
│  │      │      │  twoway2.userdata
│  │      │      │  usePointAlpha.def
│  │      │      │  usePointAlpha.init
│  │      │      │  usePointAlpha.parm
│  │      │      │  usePointAlpha.userdata
│  │      │      │  usePointColor1.def
│  │      │      │  usePointColor1.init
│  │      │      │  usePointColor1.parm
│  │      │      │  usePointColor1.userdata
│  │      │      │  uvcoords2.def
│  │      │      │  uvcoords2.init
│  │      │      │  uvcoords2.net
│  │      │      │  uvcoords2.order
│  │      │      │  uvcoords2.parm
│  │      │      │  uvcoords2.userdata
│  │      │      │  vectohvec4.def
│  │      │      │  vectohvec4.init
│  │      │      │  vectohvec4.parm
│  │      │      │  vectohvec4.userdata
│  │      │      │
│  │      │      └─uvcoords2
│  │      │              choose_S.def
│  │      │              choose_S.init
│  │      │              choose_S.parm
│  │      │              choose_S.userdata
│  │      │              choose_T.def
│  │      │              choose_T.init
│  │      │              choose_T.parm
│  │      │              choose_T.userdata
│  │      │              float2vec.def
│  │      │              float2vec.init
│  │      │              float2vec.parm
│  │      │              float2vec.userdata
│  │      │              shadingAttriUV.def
│  │      │              shadingAttriUV.init
│  │      │              shadingAttriUV.parm
│  │      │              shadingAttriUV.userdata
│  │      │              subinput1.def
│  │      │              subinput1.init
│  │      │              subinput1.parm
│  │      │              subinput1.userdata
│  │      │              suboutput1.def
│  │      │              suboutput1.init
│  │      │              suboutput1.parm
│  │      │              suboutput1.userdata
│  │      │              s_global.def
│  │      │              s_global.init
│  │      │              s_global.parm
│  │      │              s_global.userdata
│  │      │              t_global.def
│  │      │              t_global.init
│  │      │              t_global.parm
│  │      │              t_global.userdata
│  │      │              vec2float.def
│  │      │              vec2float.init
│  │      │              vec2float.parm
│  │      │              vec2float.userdata
│  │      │
│  │      └─ropnet
│  │              baketexture.chn
│  │              baketexture.def
│  │              baketexture.init
│  │              baketexture.parm
│  │              baketexture.spareparmdef
│  │              baketexture.userdata
│  │
│  ├─to_bake
│  │      object_merge1.def
│  │      object_merge1.init
│  │      object_merge1.parm
│  │      object_merge1.userdata
│  │
│  ├─__source
│  │      object_merge1.def
│  │      object_merge1.init
│  │      object_merge1.parm
│  │      object_merge1.userdata
│  │
│  └─__target
│          object_merge1.def
│          object_merge1.init
│          object_merge1.parm
│          object_merge1.userdata
│
├─out
│      baketexture1.chn
│      baketexture1.def
│      baketexture1.init
│      baketexture1.parm
│      baketexture1.spareparmdef
│      baketexture1.userdata
│      mantra_ipr.chn
│      mantra_ipr.def
│      mantra_ipr.init
│      mantra_ipr.parm
│      mantra_ipr.spareparmdef
│      mantra_ipr.userdata
│
└─tasks
    │  topnet1.def
    │  topnet1.init
    │  topnet1.net
    │  topnet1.parm
    │  topnet1.userdata
    │
    └─topnet1
            localscheduler.def
            localscheduler.init
            localscheduler.parm
            localscheduler.userdata
```
