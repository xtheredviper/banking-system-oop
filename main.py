from dataclasses import dataclass, field
from typing import List, Optional

# ======================
# Models
# ======================

@dataclass
class Usuario:
    nome: str
    data_nascimento: str
    cpf: str
    endereco: str


@dataclass
class Conta:
    agencia: str
    numero: int
    usuario: Usuario
    saldo: float = 0.0
    extrato: List[str] = field(default_factory=list)
    numero_saques: int = 0


# ======================
# Utils (Input Handling)
# ======================


def encontrar_usuario(cpf: str, usuarios: List[Usuario]) -> Optional[Usuario]:
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def ler_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("[ERROR] Please enter a valid number.")


def ler_texto(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("[ERROR] Input cannot be empty.")


# ======================
# Services (Business Logic)
# ======================


def depositar(conta: Conta, valor: float) -> str:
    if valor <= 0:
        return "[ERROR] Invalid deposit amount."

    conta.saldo += valor
    conta.extrato.append(f"Deposit: R$ {valor:.2f}")
    return "[SUCCESS] Deposit completed."



def sacar(conta: Conta, valor: float, limite: float, limite_saques: int) -> str:
    if valor <= 0:
        return "[ERROR] Invalid withdrawal amount."

    if valor > conta.saldo:
        return "[ERROR] Insufficient balance."

    if valor > limite:
        return "[ERROR] Withdrawal exceeds limit."

    if conta.numero_saques >= limite_saques:
        return "[ERROR] Withdrawal limit reached."

    conta.saldo -= valor
    conta.extrato.append(f"Withdraw: R$ {valor:.2f}")
    conta.numero_saques += 1

    return "[SUCCESS] Withdrawal completed."



def exibir_extrato(conta: Conta) -> None:
    print("\n========== STATEMENT ==========")

    if not conta.extrato:
        print("No transactions yet.")
    else:
        for item in conta.extrato:
            print(item)

    print(f"\nBalance: R$ {conta.saldo:.2f}")
    print("===============================")


# ======================
# Interface
# ======================


def menu() -> str:
    return input("""
========== MENU ==========
[d] Deposit
[s] Withdraw
[e] Statement
[nu] New User
[nc] New Account
[lc] List Accounts
[q] Quit
=> """)


# ======================
# Main Application
# ======================


def main():
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500
    AGENCIA = "0001"

    usuarios: List[Usuario] = []
    contas: List[Conta] = []

    while True:
        opcao = menu()

        if opcao == "d":
            numero = int(ler_float("Account number: "))
            conta = next((c for c in contas if c.numero == numero), None)

            if not conta:
                print("[ERROR] Account not found.")
                continue

            valor = ler_float("Deposit amount: ")
            print(depositar(conta, valor))

        elif opcao == "s":
            numero = int(ler_float("Account number: "))
            conta = next((c for c in contas if c.numero == numero), None)

            if not conta:
                print("[ERROR] Account not found.")
                continue

            valor = ler_float("Withdraw amount: ")
            print(sacar(conta, valor, LIMITE_VALOR, LIMITE_SAQUES))

        elif opcao == "e":
            numero = int(ler_float("Account number: "))
            conta = next((c for c in contas if c.numero == numero), None)

            if not conta:
                print("[ERROR] Account not found.")
                continue

            exibir_extrato(conta)

        elif opcao == "nu":
            cpf = ler_texto("CPF: ")

            if encontrar_usuario(cpf, usuarios):
                print("[ERROR] User already exists.")
                continue

            nome = ler_texto("Full name: ")
            data = ler_texto("Birth date (dd-mm-yyyy): ")
            endereco = ler_texto("Address: ")

            usuarios.append(Usuario(nome, data, cpf, endereco))
            print("[SUCCESS] User created.")

        elif opcao == "nc":
            cpf = ler_texto("User CPF: ")
            usuario = encontrar_usuario(cpf, usuarios)

            if not usuario:
                print("[ERROR] User not found.")
                continue

            numero_conta = len(contas) + 1
            conta = Conta(AGENCIA, numero_conta, usuario)
            contas.append(conta)

            print("[SUCCESS] Account created.")

        elif opcao == "lc":
            for conta in contas:
                print("-" * 30)
                print(f"Agency: {conta.agencia}")
                print(f"Account: {conta.numero}")
                print(f"Holder: {conta.usuario.nome}")

        elif opcao == "q":
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid option.")


if __name__ == "__main__":
    main()
