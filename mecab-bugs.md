# mecabでnode.surfaceが取得できないバグへの対応

「空文字列をparseした後に目的の対象の文字列をparseする」とうまくいく。

```
tagger = MeCab.Tagger('-mecabrc')
tagger.parse('') # <= 空文字列をparseする

node = tagger.parseToNode(sentence)
while node:
    print(node.surface)
    node = node.next
```
