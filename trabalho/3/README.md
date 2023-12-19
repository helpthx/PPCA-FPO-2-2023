# Questão 3 do trabalho de FPO PPCA 2/2023

## Instação

Passo a passo para instalação de requisitos Python usando pip e requirements.txt

### Requisitos

Python 3 ou superior Pip

### Passos

Se você deseja instalar as dependências em um ambiente virtual, siga estas etapas:

Crie um ambiente virtual. Você pode usar o comando virtualenv para criar um ambiente virtual:

```console 
$ virtualenv ENV 
```

Este comando criará um diretório chamado ENV que contém um ambiente virtual Python.

Ative o ambiente virtual. Para ativar o ambiente virtual, execute o seguinte comando:

```console
$ cd ENV
$ source bin/activate
```
Instale as dependências. Agora você pode instalar as dependências listadas no arquivo requirements.txt no ambiente virtual:

```console
$ pip install -r requirements.txt
```

Após concluir a instalação, você poderá começar a usar seus pacotes Python.

## Usando 

Dentro do ambiente com os requirements.txt instalados

### Usar o jupyter lab

```console
$ jupyter lab
```

Utilive a pasta de /notebooks para interagir com os notebooks criados.


## Open Source [![Open Source ](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

- [Contribution Guide](./contributing.md)
- [Style Guide](./STYLE_GUIDE.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md/)
