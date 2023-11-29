def is_palindrome(word):
 for i in range(0, int(len(word)/2)):
  if word[i] != word[len(word)-i -1]:
   return False
  return True

# Test cases
print(is_palindrome("radar"))  # Should return True
print(is_palindrome("hello"))  # Should return False
print(is_palindrome("level"))  # Should return True


# int(len("ABCD")/2) は int(4/2) であり、結果は 2 になります。これは、文字列の前半部分をループで走査するための上限を示しています。

# ループ for i in range(0, 2): では、i は 0 から 1 までの値を取ります。したがって、ループは i=0 と i=1 の2回繰り返されます。

# 条件文 if word[i] != word[len(word)-i -1]: では、word[i] は word[0] または word[1] となり、
# それは文字列の前半の各文字を指します。一方で word[len(word)-i -1] は word[4-0-1] または word[4-1-1] となり、それは文字列の後半の対応する文字（逆順）を指します。

# i=0 の場合： word[0] は "A" であり、word[len(word)-i -1] は word[4-0-1] または word[3] は "D" です。これは一致しないので、条件が成り立ちます。
# i=1 の場合： word[1] は "B" であり、word[len(word)-i -1] は word[4-1-1] または word[2] は "C" です。これも一致しないので、条件が成り立ちます。
# したがって、この文字列 "ABCD" の場合、条件が2回とも成り立ちます。つまり、"ABCD" は回文ではなく、関数は True を返すことになります。