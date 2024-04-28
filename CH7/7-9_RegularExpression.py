import re

pattern = r'[\d,]+'
text = "¥32,970"
result = re.search(pattern, text)
print(result)

if result:
    print("Search Successful.")
else:
    print("Search unsuccessful.")

#http://ccckmit.wikidot.com/regularexpression
#https://steam.oxxostudio.tw/category/python/library/re.html


# 正則表達式與輸入的理解

# 正則表達式模式 r'[\d,]+' 用於匹配一個或多個數字、逗號或空格。它由以下元素組成：

# r': 這個前綴表示字符串是原始字符串，確保反斜槓 (\) 被視為字面字符。

# []: 方括號包含一個字符類，指定模式可以匹配的一組字符。

# \d: 這個字符類匹配任何從 0 到 9 的單個數字。

# ,: 這個字面字符匹配一個逗號 (,)。

# : 這個字面字符匹配一個單個空格字符 (space)。

# +: 這個量詞指示前面的字符類或字面字符可以匹配一次或多次。

# 輸入字符串 ¥32,970 由貨幣符號 (¥)、一組數字 (32970) 以及沒有逗號或空格組成。

# 匹配機制

# 當將模式 r'[\d,]+' 應用於輸入字符串 ¥32,970 時，re.search() 函數會嘗試在字符串中找到模式的第一個匹配項。

# 初始匹配: 函數首先匹配第一個字符 ¥。但是，由於模式僅匹配數字、逗號或空格，因此此初始匹配失敗。

# 跳過不匹配字符: 函數轉到下一個字符 3。模式 \d 匹配此字符，表示成功匹配。

# 連續匹配: 函數繼續評估後續字符 2、9、7 和 0，所有這些都是數字並匹配模式 \d。

# 成功匹配: 由於模式 \d+ 需要一個或多個數字，輸入字符串中的數字序列構成成功匹配。

# 輸出和解釋

# re.search() 函數如果找到匹配項，則返回一個 Match 對象；如果沒有找到匹配項，則返回 None。在這種情況下，由於模式成功匹配數字序列，result 變量包含一個 Match 對象。

# 後續的 if 語句檢查 result 對象是否存在。如果 result 不是 None，則表示匹配成功，並打印語句 "搜尋成功"。

# 結論

# 雖然輸入字符串 ¥32,970 不包含逗號或空格，但它仍然滿足了模式 r'[\d,]+' 指定的具有至少一個數字的要求。re.search() 函數成功識別數字序列作為匹配項，導致輸出 "搜尋成功"。