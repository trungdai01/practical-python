# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of the table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        print(" ".join(f"{header:>10s}" for header in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join(f"{data:>10s}" for data in rowdata))


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def headings(self, headers):
        print(f"<tr>{''.join([f'<th>{header}</th>'for header in headers])}</tr>")

    def row(self, rowdata):
        print(f"<tr>{''.join([f'<td>{data}</td>' for data in rowdata])}</tr>")

class FormatError(Exception):
    pass


def create_formatter(fmt: str):
    """
    Process input format.
    """
    if fmt == "txt":
        formatter = TextTableFormatter()
    elif fmt == "csv":
        formatter = CSVTableFormatter()
    elif fmt == "html":
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {fmt}")
    return formatter


def print_table(data, columns, formatter):
    formatter.headings(columns)
    for obj in data:
        rowdata = [str(getattr(obj, colname)) for colname in columns]
        formatter.row(rowdata)
