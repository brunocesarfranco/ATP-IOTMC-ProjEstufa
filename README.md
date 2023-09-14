# ATP-IOTMundoConec-ProjEstufa
 Projeto desenvolvido em Python para a matéria de Internet das Coisas em um Mundo Conectado na PUCPR.

## Requisitos de Usuário
- O sistema monitora a temperatura de duas estufas distintas;
- As temperaturas são exibidas em graus Celsius (˚C);
- Há um painel (dashboard) que pode ser visualizado em um Tablet ou computador, exibindo a informação de cada estufa;
- Neste painel também há um botão que permite habilitar ou não o controle de temperatura das duas estufas;
- O sistema mantém a temperatura próxima aos 30˚C (temperatura ideal).

## Requisitos de Sistema

- Em cada estufa há um dispositivo IoT com um sensor de temperatura1;
- Para esta implementação, o dispositivo IoT (device) utilizado é seu próprio PC (execute dois projetos simultaneamente, um para cada dispositivo);
- Cada dispositivo IoT transmite para o serviço em nuvem a temperatura do interior da estufa;
- Cada dispositivo IoT controla o aquecedor de sua estufa;
- Há um painel único que mostra a temperatura das duas estufas;
- O sensor de temperatura usado é simulado, como mostrado nos vídeos 7 e 8 (antes de apresentar o Raspberry Pi). O valor da temperatura pode aumentar gradualmente enquanto o relé do aquecedor está ligado, e reduzir gradualmente quando está desligado;
- Em cada dispositivo IoT há um relé que liga e desliga um aquecedor na estufa (o relé é também simulado). O valor da temperatura pode aumentar gradualmente enquanto o relé do aquecedor está ligado, e reduzir gradualmente quando está desligado;
- O painel contém um botão que permite habilitar ou não o controle do relé do dispositivo IoT associado a este painel;
- O relé do dispositivo é acionado apenas se a temperatura daquela estufa for inferior a temperatura ideal e o botão do painel estiver ligado (habilitado);
- O protocolo de comunicação a ser utilizado deve ser o MQTT;
- O serviço em nuvem utilizado será o Cayenne myDevices (www.cayenne.mydevices.com);

## Digrama de arquitetura
![image](https://github.com/brunocesarfranco/ATP-IOTMundoConec-ProjEstufa/assets/80123383/c2a671dc-759f-40f1-8564-f5fdd80b5580)

## Detalhes tecnicos
- IDE utilizada: Visual Studio Code
- Linguagem: Python 3.8.1

## Adicionais
- Caso tenha dificuldade em importar o pacote mqtt, utilize o comando "pip3 install paho-mqtt" no terminal da IDE.
- Em caso de reutilização do codigo, altere a variavel "client_id" para satisfazer as condições para conexão.
- Link para o manager broker (MQTT): https://www.hivemq.com/demos/websocket-client/
