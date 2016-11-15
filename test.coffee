#Declarations
greet1 = -> 'This is a greeting function.'
greet2 = (mood) -> "I feel #{mood}!"
cube = (num) -> Math.pow num, 5

console.log do -> 'hello me'

#Can call a function either way
console.log greet1()
console.log do greet1

#Functions
console.log greet2 'silly'

