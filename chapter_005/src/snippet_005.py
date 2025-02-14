import typing
from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def main():

    # read the Document
    doc: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    # check whether we have read a Document
    assert doc is not None

    # print the text on the first Page
    print(l.get_text_for_page(0))


if __name__ == "__main__":
    main()
