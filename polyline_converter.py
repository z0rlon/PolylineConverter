import click
from typing import List, Tuple


def parse_vector(token: str) -> Tuple[int, int, int]:
    token = token.strip().strip('()')
    parts = token.split(',')
    if len(parts) != 3:
        raise click.BadParameter(f"Invalid vector format: {token}")
    return tuple(int(p.strip()) for p in parts)


def convert_vectors(vectors: List[Tuple[int, int, int]],
                    params: Tuple[int, int, int],
                    thresholds: Tuple[int, int, int],
                    names: Tuple[str, str, str]) -> str:
    result_vectors = []
    for vec in vectors:
        converted = []
        for i, value in enumerate(vec):
            if value >= thresholds[i]:
                diff = params[i] - value
                converted.append(f"{names[i]} - {diff}")
            else:
                converted.append(str(value))
        result_vectors.append(f"({','.join(converted)})")
    return ','.join(result_vectors)


@click.command()
@click.option('--vectors', '-v', required=True, help='Comma separated list of vectors like "(1,2,3),(4,5,6)"')
@click.option('--params', '-p', nargs=3, type=int, required=True, help='Max dimensions for X Y Z')
@click.option('--thresholds', '-t', nargs=3, type=int, required=True, help='Threshold values for X Y Z')
@click.option('--names', '-n', nargs=3, default=('Param1', 'Param2', 'Param3'), help='Parameter names for X Y Z')
def main(vectors: str, params: Tuple[int, int, int], thresholds: Tuple[int, int, int], names: Tuple[str, str, str]):
    vec_tokens = [tok for tok in vectors.split(')') if tok.strip()]
    parsed_vectors = [parse_vector(tok + ')') for tok in vec_tokens]
    result = convert_vectors(parsed_vectors, params, thresholds, names)
    click.echo(result)


if __name__ == '__main__':
    main()
