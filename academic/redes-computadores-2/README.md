# 🌐 Redes de Computadores II (Sistemas de Informação - IFTO)

Este diretório reúne um conjunto de simulações e projetos de infraestrutura de redes desenvolvidos utilizando o **Cisco Packet Tracer**. As atividades cobrem tópicos avançados de endereçamento IP (VLSM), roteamento estático, protocolos de roteamento dinâmico (RIP e OSPF), integração wireless e arquiteturas corporativas baseadas em switches multicamada (Layer 3).

---

## 🛠️ Como Executar os Laboratórios

Para abrir e interagir com as simulações, você precisará ter o **Cisco Packet Tracer** instalado.

1. Baixe e instale a versão oficial através do portal [Cisco Networking Academy](https://www.netacad.com/).
2. Faça o clone do repositório. Como este repositório possui caráter acadêmico completo e pessoal, você pode optar por clonar **apenas este diretório** utilizando o recurso de *Sparse Checkout* do Git para economizar espaço e manter a privacidade:
   ```bash
   # Clone minimalista sem baixar os arquivos
   git clone --filter=blob:none --no-checkout https://github.com/pedrolabre/pedrolabre.git
   cd pedrolabre

   # Configure o Git para baixar apenas esta pasta
   git sparse-checkout set academic/redes-computadores-2

   # Baixe os arquivos selecionados
   git checkout
   ```
3. Navegue até este diretório (`academic/redes-computadores-2`) e abra qualquer arquivo `.pkt` com dois cliques para carregar a topologia e verificar a configuração dos dispositivos no CLI.

---

## 📂 Laboratórios e Simulações

Abaixo estão detalhados os objetivos, estruturas de rede e configurações lógicas implementadas em cada arquivo de laboratório:

### 1. 📝 [Aula 12 maio 2025 - Atividade Avaliativa - Roteamento Estatico.pkt](./Aula%2012%20maio%202025%20-%20Atividade%20Avaliativa%20-%20Roteamento%20Estatico.pkt)
* **Objetivo**: Implementar o endereçamento IP de sub-redes e configurar rotas estáticas para interligar filiais distantes em um ambiente de avaliação.
* **Topologia**:
  - **3 Roteadores Cisco**: Interconectados por links seriais/ponto a ponto (`10.109.5.0/30` e `10.109.6.0/30`).
  - **4 Ambientes Locais**: Cada um segmentado com switches dedicados (`Switch Ambiente 01` a `04`).
  - **Serviços**: Servidores de DHCP e DNS configurados para distribuir endereços automaticamente para os hosts.
* **Esquema de Endereçamento (Sub-redes 10.109.x.x)**:
  - `10.109.1.0/25` e `10.109.2.0/25` (Redes locais do Router 4).
  - `10.109.3.0/25` (Rede local do Router 5).
  - `10.109.4.0/26` (Rede local do Router 7).
* **Configuração de Roteamento (Cisco IOS)**:
  - **Router 4**: `ip route 10.109.3.0 255.255.255.128 10.109.5.2`
  - **Router 5**: Rotas para alcançar as sub-redes locais do Router 4 via link 5.1, e para a sub-rede do Router 7 via link 6.2:
    - `ip route 10.109.1.0 255.255.255.128 10.109.5.1`
    - `ip route 10.109.2.0 255.255.255.128 10.109.5.1`
    - `ip route 10.109.4.0 255.255.255.192 10.109.6.2`

---

### 2. ⚡ [Aula 19 maio 2025 - Roteamento Dinamico RIP.pkt](./Aula%2019%20maio%202025%20-%20Roteamento%20Dinamico%20RIP.pkt)
* **Objetivo**: Substituir o gerenciamento manual das rotas estáticas pela configuração do protocolo dinâmico **RIP (Routing Information Protocol)**, facilitando a convergência da rede em caso de falha de enlaces.
* **Topologia**: Mantém a infraestrutura de 3 roteadores e 4 ambientes locais da aula anterior.
* **Configuração de Roteamento (Cisco IOS)**:
  - Ativação do protocolo RIP com declaração de redes no escopo classful `10.0.0.0`. Os roteadores compartilham automaticamente suas tabelas com vizinhos diretos baseados em vetor de distância (limite de 15 saltos).
  - Configuração do RIP para evitar a sumarização automática (`no auto-summary`), garantindo o suporte a VLSM em sub-redes `/25` e `/26`.

---

### 3. ⚖️ [Aula 02 junho 2025 - Roteamento RIP e OSPF.pkt](./Aula%2002%20junho%202025%20-%20Roteamento%20RIP%20e%20OSPF.pkt)
* **Objetivo**: Laboratório comparativo avançado para analisar as diferenças de projeto, métricas e convergência entre um protocolo de vetor de distância (RIP) e um de estado de enlace (**OSPF - Open Shortest Path First**).
* **Estrutura**:
  - Apresenta topologias espelhadas no mesmo canvas de simulação.
  - Uma área roda inteiramente sob o protocolo **RIP**, enquanto a outra área equivalente está configurada com o processo **OSPF** de área única (`OSPF Area 0`).
* **Configuração OSPF (Cisco IOS)**:
  - Declaração de `router ospf 1` nos roteadores.
  - Mapeamento das sub-redes com máscara curinga (wildcard masks) para restringir o tráfego de anúncios OSPF à Area 0:
    - Exemplo no Router 4: `network 10.109.1.0 0.0.0.127 area 0`
    - Configuração de IDs de roteador exclusivos (`router-id`) para eleições de DR/BDR.

---

### 4. 📶 [Aula 02 junho 2025 - Roteamento RIP-OSPF + Rede Wireless.pkt](./Aula%2002%20junho%202025%20-%20Roteamento%20RIP-OSPF%20%2B%20Rede%20Wireless.pkt)
* **Objetivo**: Integrar redes locais sem fio (**WLAN**) à infraestrutura de roteamento dinâmico RIP/OSPF comparativo.
* **Topologia**:
  - Incorpora os três grupos de roteadores (básico, RIP e OSPF) da aula de 02 de junho.
  - Integração de roteadores sem fio e Access Points em um dos switches dos ambientes de sub-rede.
* **Configuração**:
  - Definição de SSID de redes locais, tempos de concessão e distribuição automática de endereços IP via DHCP para hosts móveis (smartphones e laptops) que circulam pela topologia.

---

### 5. 📈 [Aula 16 junho 2025 - Expansao RIP-OSPF (Nova Subrede).pkt](./Aula%2016%20junho%202025%20-%20Expansao%20RIP-OSPF%20%28Nova%20Subrede%29.pkt)
* **Objetivo**: Praticar a expansão física de uma infraestrutura existente e validar se os protocolos de roteamento dinâmico (OSPF/RIP) realizam o anúncio correto da nova rede para toda a topologia de forma automatizada.
* **Modificações**:
  - Adição de uma nova interface física ativa no Roteador 7 (`GigabitEthernet0/2`), configurada com a sub-rede `10.109.7.1/26`.
  - Configuração do anúncio dessa nova rede no processo OSPF (`network 10.109.7.0 0.0.0.63 area 0`) e no processo RIP correspondente.
* **Validação**: Testes de ping originados de ambientes do Roteador 4 direcionados ao novo segmento `10.109.7.0/26` no Roteador 7, testando o recálculo do algoritmo de Dijkstra (OSPF).

---

### 6. 🎓 [Aula 23 junho 2025 - Revisao e Consolidadacao RIP-OSPF.pkt](./Aula%2023%20junho%202025%20-%20Revisao%20e%20Consolidadacao%20RIP-OSPF.pkt)
* **Objetivo**: Laboratório de fechamento de bimestre para consolidação prática. Engloba toda a arquitetura de roteamento dinâmico, segurança, wireless e redundância.
* **Estrutura**:
  - Rede corporativa multicâmpus unificada.
  - Combinação de RIP, OSPF, rotas estáticas padrão (default routes) e balanceamento de carga de dados inter-redes.
* **Principais Recursos Configurados**:
  - Propagação de rotas padrão com `default-information originate` no OSPF.
  - DHCP pools locais gerenciando a entrega automática de conexões sem fio e cabeadas.
  - Tabela de rotas otimizada para garantir a menor latência no envio de pacotes.

---

### 7. 🎯 [Atividade Avaliativa - Enderecamento e Subnetting (Template).pkt](./Atividade%20Avaliativa%20-%20Enderecamento%20e%20Subnetting%20%28Template%29.pkt)
* **Objetivo**: Template de topologia inicial desenvolvido inteiramente por mim para planejar a segmentação física de sub-redes (VLSM) e o endereçamento IP estático das interfaces físicas antes da implementação e testes de rotas.
* **Estrutura**:
  - Contém 3 Roteadores Cisco e 4 Switches segmentando ambientes de TI.
  - Interfaces físicas dos roteadores configuradas com seus respectivos IPs na faixa privada de `192.168.1.0/24` a `192.168.4.0/24` (ex: sub-redes `/25` e `/26`).
  - Sem protocolos de roteamento ativos, servindo como base limpa para simular a resolução de problemas de conectividade.

---

### 8. 🏢 [Topologia Corporativa com Multilayer Switches.pkt](./Topologia%20Corporativa%20com%20Multilayer%20Switches.pkt)
* **Objetivo**: Simulação avançada de redes locais de campus (Enterprise LAN) com foco em **Layer 3 Switching (Switches Multicamada)** para gerenciar roteamento inter-VLAN com alta performance.
* **Topologia**:
  - **2 Switches Multicamada Cisco 3560**: Atuando no núcleo da rede local (Core/Distribution layer).
  - **3 Switches Comuns Cisco 2960**: Camada de acesso (Access layer) dividindo hosts locais.
  - **3 Roteadores Cisco**: Gerenciando o tráfego de saída (borda) para WAN/Internet.
* **Conceitos e Comandos Implementados**:
  - Habilitação do roteamento IP interno nos switches L3 (`ip routing`).
  - Configuração de **Interfaces Virtuais de Switch (SVIs)** para as VLANs do campus (ex: `interface Vlan10`, `interface Vlan20`), atribuindo endereços IP para funcionarem como os gateways padrão das redes locais.
  - Configuração de entroncamento IEEE 802.1Q (`switchport mode trunk`) para interconexão e tráfego simultâneo de VLANs.
  - Redundância e alta velocidade sem gargalos de CPU comuns a topologias tradicionais de roteador único (Router-on-a-Stick).
