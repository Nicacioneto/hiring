# Hiring
Projeto exclusivo para processo seletivo

## Instruções
1. Faça um fork desse projeto
2. Resolva o problema da forma mais simples que conseguir
3. Quando tiver terminado, me envie um pull request
4. Pronto :)

## Instruções de execução
1. Declare as variáveis de ambiente
    Por motivos de segurança as variáveis BLOCKIO_API_KEY e o BLOCKIO_PIN estão sendo utilizadas a partir de variáveis de ambiente, portanto antes de executar o teste atribua valores a essas duas variáveis:
    
    > export BLOCKIO_API_KEY="sua api key"
    
    > export BLOCKIO_PIN="seu pin"
2. Instale os requisitos para rodar o sistema. Essa informação está no arquivo requirements.txt

3. Para Transferir o BTCT para a carteira definida execute o script transacao_main.py, ele transferirá 1 BTCT para a carteira. (minha conta só tem 2.9 BTCT, só poderá ser feito 2 vezes com esse valor).

4. Rode os testes.

    > python transacao_test.py

5. Utilizar os métodos definidos em transacao.py como preferir. 
    O método setup inicia o bloco de transacões com suas informações;

    O método check_balance retorna o dictionaire com as informações do balanço da conta que foi consultada.

    O método send_cryptocoin faz uma retirada de cryptomoeda de uma carteira para outra.


## Objetivo
Realizar transação de Bitcoin Testnet usando API

## Descrição
1. Faça um script que envie 1 unidade de **Bitcoin Testnet** para a seguinte carteira usando a API do [Block.io](https://block.io). Pode ser em Ruby, Python ou Javascript. Faça da forma mais simples que conseguir. Não precisa ter interface com o usuário.
2. Faça um teste unitário que asserte a realização da transação.

Carteira:
> mnYoahiweETgdXsfY92GCWA6HoRj9knQUw
