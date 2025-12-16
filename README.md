# Redes de Computadores

Este repositório contém as implementações práticas e resoluções de exercícios desenvolvidas para a disciplina de **Redes de Computadores**, ministrada pelo professor Marcos Fagundes Caetano no semestre 2024.1 na Universidade de Brasília (UnB).

O foco dos materiais aqui presentes é a aplicação prática de conceitos de comunicação de dados, utilizando a linguagem **Python** para ilustrar o funcionamento de protocolos e aplicações de rede.

## Organização do Repositório:

- **`BBA`**: Implementação do algoritmo *Bandwidth-Based Adaptation* (BBA). Este projeto foca em algoritmos de bitrate adaptativo (ABR) para streaming de vídeo, simulando a adaptação da qualidade de reprodução com base na largura de banda disponível.
- **`Lista-de-Exercicios-Fechamento-Capítulo-2`**: Conjunto de exercícios práticos e scripts referentes ao fechamento do Capítulo 2 (Camada de Aplicação), abordando conceitos fundamentais de protocolos de aplicação.

## 📚 Detalhamento Técnico

### 📂 BBA (Bandwidth-Based Adaptation)
Implementação de um algoritmo de **Adaptive Bitrate Streaming (ABR)** do lado do cliente. O código simula a lógica de decisão de players de vídeo modernos (como YouTube/Netflix).
* **Mecanismo:** O algoritmo calcula uma estimativa da largura de banda disponível baseada na média harmônica dos fragmentos passados.
* **Lógica de Controle:** Implementa uma máquina de estados que decide entre ser "conservadora" (mantendo qualidade baixa para encher o buffer) ou "agressiva" (subindo a qualidade quando o buffer está seguro), visando evitar o *stalling* (travamento) da reprodução.

### 📂 Lista-de-Exercicios (Socket Programming)
Desenvolvimento de aplicações de rede utilizando a API de Sockets do sistema operacional (Berkeley Sockets).
* **Protocolos de Transporte:**
    * **TCP:** Criação de *streams* de dados confiáveis, com tratamento de *handshake* (3-way) e garantia de ordem de entrega. Usado para simular transferências de arquivos ou chats.
    * **UDP:** Implementação de envio de datagramas sem conexão (*best-effort*), ideal para simulações de aplicações sensíveis a latência.
* **Serialização:** Uso de `structs` ou codificação JSON para encapsular dados da camada de aplicação antes do envio pelo socket.
