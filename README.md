<div align="center">

[<img src="https://media.discordapp.net/attachments/1213992791508779019/1263553833284538399/iu.png?ex=669aa7b5&is=66995635&hm=7502dd555f93805cdc749a01cf97f4a93386d4ec62faa0ab4521a92a2977166c&format=webp&quality=lossless&width=472&height=314&" width="750" />](https://media.discordapp.net/attachments/1213992791508779019/1263553833284538399/iu.png?ex=669aa7b5&is=66995635&hm=7502dd555f93805cdc749a01cf97f4a93386d4ec62faa0ab4521a92a2977166c&format=webp&quality=lossless&width=472&height=314&)

</div>

### PassWord Generator:


Para o gerador de senhas eu utilizei a biblioteca random e seus módulos join e sample, criei 3 váriaveis, sendo elas uma contendo o alfabeto de A-Z maiúsculo outra tendo o alfabeto de A-Z minúsculos e uma váriavel com numeros em strings de 0 a 9, criei um input para que o usuário defina o tanto de caracteres que ele tenha em sua senha, e defini que a senha seria a junção das 3 váriaveis, criei a def generator que vai gerar a senha, defini a senha gerada, em que seria embaralhada entre as 3 váriaveis de alfabeto e numero e com o sample eu defini seu tamanho sendo ele no digitado no input.

 ### Observações:

 É opcional, mas pode criar uma variável chamada "symbols" com simbolos por exemplo "@#$&)(" e acrescentar na váriavel password.

Exemplo
   ````py
upper_words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_words = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "@#$%&*[()"

password_chars = int(input("How many characters will your password have:"))

password = upper_words + lower_words + numbers + symbols

def generator(password):
  password = "".join(random.sample(password, password_chars))
  print(password)
  #Aqui o "".join é preciso para que quando a senha seja gerada, ela não fique com espaços entre os caracteres. 

