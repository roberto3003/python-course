amazon_cart = [
        'notebooks',
        'sunglasses',
        'toys',
        'grapes'
        ]

print(amazon_cart)
print(hex(id(amazon_cart)))
print(amazon_cart[1]) #sunglasses
print(amazon_cart[0::2]) #notebooks, toys
print(amazon_cart[1::2]) #sunglasses, grapes

amazon_cart[-1] = 'lemons'
print(amazon_cart[-1])
print(amazon_cart)
print(hex(id(amazon_cart)))
