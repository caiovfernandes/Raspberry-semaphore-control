**Aluno**: Caio Vinicius Fernandes de Araujo
**Matricula**: 170138798


# Instruções


## 1. Inicie o servidor distribuido:
```bash
python3 distributed_server/src/main.py
```

## 2. Inicie o servidor central:
```bash
python3 central_server/src/main.py
```

## 2. Selecione a opções desejada:
- **1** para modo noturno.
- **2** para modo emergencia.
- **3** para modo padrão.
- **4** para modo Debug.


# Funcionalidades implementadas - Completas
1. Mecanismo de acionar e desacionar o Modo de emergência e o Modo noturno.
2. Controle do mecanismo de temporização dos semáforos seguindo a temporização.
3. Correta implementação de comunicação entre os servidores usando o protocolo TCP/IP.
4. Utilização de boas práticas como o uso de bons nomes, modularização e organização em geral, bom desempenho da aplicação sem muito uso da CPU.

# Funcionalidade implementadas - Incompletas:
1. Detecção dos botões de travessia de pedestres reduzindo o tempo de abertura do semáforo (incluindo o debounce). (Detecção dos botões + debouncing)