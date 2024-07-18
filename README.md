### PassWord Generator:


Para o gerador de senhas eu utilizei a biblioteca random e seus módulos join e sample, criei 3 váriaveis, sendo elas uma contendo o alfabeto de A-Z maiúsculo outra tendo o alfabeto de A-Z minúsculos e uma váriavel com numeros em strings de 0 a 9, criei um input para que o usuário defina o tanto de caracteres que ele tenha em sua senha, e defini que a senha seria a junção das 3 váriaveis, criei a def generator que vai gerar a senha, defini a senha gerada, em que seria embaralhada entre as 3 váriaveis de alfabeto e numero e com o sample eu defini seu tamanho sendo ele no digitado no input

Exemplo
   ````py
def generator(password):
  password = "".join(random.sample(password, password_chars))
  print(password)
  #Aqui o "".join é preciso para que quando a senha seja gerada, ela não fique com espaços entre os caracteres. 
