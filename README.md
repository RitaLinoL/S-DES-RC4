# S-DES-RC4
Atividade Prática da disciplina de Segurança de Redes, ofertada pelo professor Silvio Sampaio na UFRN

Alunas: Alice Soares Pereira de Barros e Rita de Cássia Lino Lopes

### 1 - Algoritmo S-DES
Implemente o algoritmo de criptografia S-DES apresentado em aula para cifrar/decifrar um
arquivo texto passado por parâmetro em linha de comando.

### 2 - Algoritmo RC4
Implementar o protótipo do algoritmo RC4 para cifra qualquer texto usando uma chave de
tamanho variável entre 1 a 256 bytes.

### 3 - Socket e Servidor
Desenvolva uma aplicação para troca de mensagens de texto (estilo chat) entre você e
seus colegas de maneira que seja possível trocar mensagens de texto entre pares
utilizando criptografia com o S-DES e o RC4, desenvolvidos por você.
  - Assuma que a comunicação será feita pela porta 5354, com socket TCP
  
  - Assuma também que ambos os pares já conhecem a chave de segurança e essa poderá ser
modificada pelo usuário em tempo de execução da aplicação, bem como o algoritmo de
criptografia utilizado (S-DES ou RC4).

### 4 - Troca de chaves Diffie-Helman
Usando comunicação via socket, implemente a troca de chaves de sessão baseado no
modelo de Diffie-Hellman.
  - Adicione esta funcionalidade ao seu chat seguro
  
  - Com esta atualização, seu programa deverá permitir configurar os valores de q e α; e trocar
AUTOMATICAMENTE as chaves a serem usadas na sessão de criptografia simétrica.
