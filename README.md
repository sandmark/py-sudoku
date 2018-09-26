# Pythonで数独解決
習作です。

`python sudoku.py`

と実行することで問題を入力するようプロンプトが出ます。

```
> 200000009
> 904600031
> 000540000
> 800050000
> 040000010
> 096280750
> 078405902
> 061908004
> 000000000
```

すでに数字が入っているマスには数字を、空欄には 0 を指定します。入力が終わると自動的に解を求め始めます。なお、解の存在しない問題については考慮していません。

## アルゴリズム
[M.Hiroi's Home Page](mhiroi)で解説されていた例を参考にさせていただきました。この場を借りて感謝を申し上げます。

## ToDo
- 再帰から抜ける手段が`try ~ except`なのでなんとかしたい

## ChangeLog
### 0.0.1
Initial Release.

[mhiroi]: http://www.geocities.jp/m_hiroi/
