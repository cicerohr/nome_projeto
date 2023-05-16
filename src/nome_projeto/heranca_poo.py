"""Projeto para testar a documentação automática do MkDocs-material com o
plugin mkdocstrings.

Exemplo com herança POO.

Quote: Fonte da classe
    @author: Fábio Kon

    @modified by: Cícero

    @link: https://gitlab.com/ccsl-usp/LabPOO/-/blob/master/heranca/poligono.py
"""
from abc import ABC, abstractmethod


class Poligono(ABC):
    """Classe abstrata base para um polígono."""

    def __init__(self, nome: str, numero_de_lados: int) -> None:
        """Inicializador do objeto Polígono.

        Parameters:
            nome: nome do polígono
            numero_de_lados: quantidade de lados do polígono
        """
        self.nome = nome
        self.numero_de_lados = numero_de_lados
        self.lados = [0 for _ in range(numero_de_lados)]

    def eh_regular(self) -> bool:
        """Verifica se o polígono é regular.

        Tip: Dica
            Um polígono é regular se todos os lados são iguais.

        Returns:
            Verdadeiro se o polígono é regular
        """
        return len(set(self.lados)) == 1

    def obter_lados(self) -> None:
        """Obtém os valores dos lados do polígono."""
        self.lados = [
            float(input(f'{self.nome} - Lado {str(lado + 1)}: '))
            for lado in range(self.numero_de_lados)
        ]

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula a área do polígono.

        Método abstrato que gera uma exceção para exigir que classes
        derivadas substituam esse método.

        Returns:
            Área do polígono

        Raises:
            NotImplementedError: Subclasses precisam implementar o método
                                calcular_area()
        """
        raise NotImplementedError(
            'Subclasses precisam implementar o método calcular_area()'
        )

    def calcular_perimetro(self) -> float:
        """Calcula o perímetro de um polígono.

        Returns:
            Perímetro do polígono
        """
        return sum(self.lados)

    def numero_de_diagonais(self) -> int:
        """Calcula o número de diagonais do polígono.

        Sendo:
            n -> número de lados do polígono\n
            D = n(n - 3) / 2

        Returns:
            Número de diagonais do polígono
        """
        return (self.numero_de_lados * (self.numero_de_lados - 3)) // 2

    def __repr__(self) -> str:
        """Representação do objeto."""
        return (
            f'{self.__class__.__name__}()\n'
            f'{self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}\n'
        )


class Triangulo(Poligono):
    """Classe que representa um triângulo.

    Examples: Exemplos
        >>> triangulo = Triangulo()
        >>> triangulo.lados = [3, 4, 5]
        >>> triangulo.nome
        'Triângulo'
        >>> triangulo.eh_triangulo()
        True
        >>> triangulo.eh_regular()
        False
        >>> triangulo.determinar_tipo_triangulo_lados()
        'escaleno'
        >>> triangulo.calcular_area()
        6.0
        >>> triangulo.calcular_perimetro()
        12
        >>> triangulo.numero_de_diagonais()
        0
    """

    def __init__(self) -> None:
        """Inicializador do objeto Triangulo."""
        self.nome = 'Triângulo'
        # chama o inicializador da classe pai (Polígono)
        super().__init__(self.nome, 3)

    def eh_triangulo(self) -> bool:
        """Verifica se os lados formam um triângulo.

        Tip: Dica
            Só irá existir um triângulo se, e somente se, os seus lados
            obedeceram à seguinte regra: um de seus lados deve ser maior que o
            valor absoluto (módulo) da diferença dos outros dois lados e menor
            que a soma dos outros dois lados.
            Veja o resumo da regra abaixo:

            | b - c | < a < b + c\n
            | a - c | < b < a + c\n
            | a - b | < c < a + b

        Returns:
            True se os lados formam um triângulo e False se não.
        """
        a, b, c = self.lados
        if a + b > c and a + c > b and b + c > a:
            return True
        return False

    def determinar_tipo_triangulo_lados(self) -> str:
        """Determina o tipo de triângulo quanto aos lados.

        Tip: Dica
            Equilátero - todos os lados são iguais\n
            Isósceles - dois dos lados são iguais\n
            Escaleno - todos os lados são diferentes

        Returns:
            Tipo de triângulo
        """
        a, b, c = self.lados
        if a == b and b == c and c == a:
            return 'equilátero'
        if a == b or b == c or c == a:
            return 'isósceles'
        return 'escaleno'

    def calcular_area(self) -> float:
        """Calcula a área do triângulo utilizando a fórmula de Heron.

        Tip: Dica
            Fórmula de Heron:

            A = √p.(p - a).(p - b).(p - c), onde 'p' é o semiperímetro dado
            pela fórmula p = (a + b + c) / 2

        Returns:
            Área do triângulo
        """
        a, b, c = self.lados
        # calcula o semiperímetro
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do triângulo."""
        a, b, c = self.lados
        if self.eh_triangulo():
            return (
                f'{self.nome} de lados {a}, {b} e {c} tem:\n'
                f'\tÁrea: {self.calcular_area():0.2f}\n'
                f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
                f'\tTipo: {self.determinar_tipo_triangulo_lados()}\n'
                f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
            )
        return f'Os lados {a}, {b} e {c} não formam um triângulo.'


class TrianguloRetangulo(Triangulo):
    """Representa um triângulo retângulo.

    Examples: Exemplos
        >>> triangulo_retangulo = TrianguloRetangulo()
        >>> triangulo_retangulo.lados = [3, 4, 5]
        >>> triangulo_retangulo.nome
        'Triângulo Retângulo'
        >>> triangulo_retangulo.eh_triangulo()
        True
        >>> triangulo_retangulo.eh_triangulo_retangulo()
        True
        >>> triangulo_retangulo.eh_regular()
        False
        >>> triangulo_retangulo.determinar_tipo_triangulo_lados()
        'escaleno'
        >>> triangulo_retangulo.calcular_area()
        6.0
        >>> triangulo_retangulo.calcular_perimetro()
        12
        >>> triangulo_retangulo.numero_de_diagonais()
        0
    """

    def __init__(self) -> None:
        """Inicializador do objeto TrianguloRetangulo."""
        # chama o inicializador da classe pai (Triangulo)
        super().__init__()
        self.nome = 'Triângulo Retângulo'

    def eh_triangulo_retangulo(self) -> bool:
        """Verifica se os lados formam um triângulo retângulo.

        Fórmula de Pitágoras:
            a² = b² + c²

        Returns:
            True se os lados formam um triângulo retângulo e False se não
        """
        a, b, c = self.lados
        return (
            a**2 == b**2 + c**2
            or b**2 == a**2 + c**2
            or c**2 == a**2 + b**2
        )

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do triângulo retângulo."""
        a, b, c = self.lados
        if self.eh_triangulo() and self.eh_triangulo_retangulo():
            return (
                f'{self.nome} de lados {a}, {b} e {c} tem:\n'
                f'\tÁrea: {self.calcular_area():0.2f}\n'
                f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
                f'\tTipo: {self.determinar_tipo_triangulo_lados()}\n'
            )
        return f'Os lados {a}, {b} e {c} não formam um triângulo retângulo.'


class Retangulo(Poligono):
    """Classe que representa um retângulo.

    Examples: Exemplos
        >>> retangulo = Retangulo()
        >>> retangulo.lados = [3, 4]
        >>> retangulo.nome
        'Retângulo'
        >>> retangulo.eh_regular()
        False
        >>> retangulo.calcular_area()
        12
        >>> retangulo.calcular_diagonal()
        5.0
        >>> retangulo.calcular_perimetro()
        7
        >>> retangulo.numero_de_diagonais()
        2
    """

    def __init__(self) -> None:
        """Inicializador do objeto Retangulo."""
        self.nome = 'Retângulo'
        # chama o inicializador da classe pai (Polígono)
        super().__init__(self.nome, 4)

    def obter_lados(self):
        """Obtém os valores dos lados do retângulo."""
        lado1 = float(input(f'{self.nome} - Lado 1: '))
        lado2 = float(input(f'{self.nome} - Lado 2: '))
        self.lados = [lado1, lado2, lado1, lado2]

    def calcular_area(self) -> float:
        """Calcula a área do retângulo.

        Onde:
            A -> área do retângulo\n
            b -> base\n
            h -> altura

            A = b . h

        Returns:
            Área do retângulo
        """
        return self.lados[0] * self.lados[1]

    def calcular_diagonal(self) -> float:
        """Calcula a diagonal do retângulo.

        Fórmula de Pitágoras:
            a² = b² + c²

        Returns:
            Diagonal do retângulo
        """
        return (self.lados[0] ** 2 + self.lados[1] ** 2) ** 0.5

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do retângulo."""
        return (
            f'{self.nome} de {self.lados[0]}x{self.lados[1]} tem:\n'
            f'\tÁrea: {self.calcular_area():0.2f}\n'
            f'\tPerímetro: {self.calcular_perimetro():0.2f}\n'
            f'\tDiagonal: {self.calcular_diagonal():0.2f}\n'
            f'\tNúmero de diagonais: {self.numero_de_diagonais()}\n'
            f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
        )


class Trapezio(Poligono):
    """Classe que representa um trapézio.

    Examples: Exemplos
        >>> trapezio = Trapezio()
        >>> trapezio.lados = [3, 4, 5, 6]
        >>> trapezio.nome
        'Trapézio'
        >>> trapezio.eh_regular()
        False
        >>> trapezio.calcular_area()
        56.92099788303083
        >>> trapezio.altura()
        16.26314225229452
        >>> trapezio.numero_de_diagonais()
        2
    """

    def __init__(self) -> None:
        """Inicializador do objeto Trapézio."""
        self.nome = 'Trapézio'
        # chama o inicializador da classe pai (Polígono)
        super().__init__(self.nome, 4)

    def obter_lados(self) -> None:
        """Obtém os valores dos lados do trapézio."""
        base_maior = float(input(f'{self.nome} - Base maior: '))
        base_menor = float(input(f'{self.nome} - Base menor: '))
        lado1 = float(input(f'{self.nome} - Lado 1: '))
        lado2 = float(input(f'{self.nome} - Lado 2: '))
        self.lados = [base_maior, base_menor, lado1, lado2]

    def calcular_area(self) -> float:
        """Calcula a área do trapézio.

        Tip: Dica
            Fórmula de Heron:

            A = √p.(p - a).(p - b).(p - c), onde 'p' é o semiperímetro dado
            pela fórmula p = (a + b + c) / 2

        Returns:
            Área do trapézio
        """
        base_maior = self.lados[0]
        base_menor = self.lados[1]
        lado1 = self.lados[2]
        lado2 = self.lados[3]
        semiperimetro = (base_maior + base_menor + lado1 + lado2) / 2
        return (
            semiperimetro
            * (semiperimetro - base_maior)
            * (semiperimetro - base_menor)
            * (semiperimetro - lado1)
            * (semiperimetro - lado2)
        ) ** 0.5

    def altura(self) -> float:
        """Calcula a altura do trapézio.

        A partir da área do trapézio e das bases, calcula a altura.

        Sendo:
            A -> área do trapézio\n
            h -> altura\n
            B -> base maior\n
            b -> base menor\n
            A = h * (B + b) / 2 ∴ h = 2 * A / (B + b)

        Returns:
            Altura do trapézio
        """
        return (self.calcular_area() * 2) / (self.lados[0] + self.lados[1])

    def __str__(self) -> str:
        """Retorna uma ‘string’ com os dados do trapézio.

        Returns:
            Dados do trapézio
        """
        return (
            f'{self.nome} - base maior: {self.lados[0]}; '
            f'base menor: {self.lados[1]}; '
            f'lado 1: {self.lados[2]}; '
            f'lado 2: {self.lados[3]}\n'
            f'\tÁrea: {self.calcular_area():.2f}\n'
            f'\tPerímetro: {self.calcular_perimetro():.2f}\n'
            f'\tNúmero de diagonais: {self.numero_de_diagonais()}\n'
            f'\tAltura: {self.altura():.2f}\n'
            f'\tÉ regular? {"sim" if self.eh_regular() else "não"}\n'
        )


def main():
    """Função principal."""
    # retangulo = Retangulo()
    # retangulo.obter_lados()
    # print(retangulo)
    # print(repr(retangulo))
    triangulo = Triangulo()
    triangulo.obter_lados()
    print(triangulo)
    print(repr(triangulo))
    # triangulo_retangulo = TrianguloRetangulo()
    # triangulo_retangulo.obter_lados()
    # print(triangulo_retangulo)
    # print(repr(triangulo_retangulo))
    trapezio = Trapezio()
    trapezio.obter_lados()
    print(trapezio)
    print(repr(trapezio))


if __name__ == '__main__':
    main()
