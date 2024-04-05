dict={
    "APPLE":"IT IS A FRUIT ",

    "CAT":"IT IS A ANIMAL",

    "TIGER":"IT IS A CARNIVOROUS ANIMAL",

    "LION":"KING OF THE JUNGLE",

    "TORTOISE":"IT IS A REPLTILE "

}
print("OPTIONS  ARE",dict.keys()) #display keys 
a=input("ENTER THE WORD FROM LIST :")
print("THE MEANING OF YOUR WORD IS:",dict.get(a))#this will take keys and display value


 