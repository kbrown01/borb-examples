import typing

from borb.io.read.types import Name, String, Dictionary
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
from borb.toolkit.text.tf_idf_keyword_extraction import TFIDFKeywordExtraction
from borb.toolkit.text.stop_words import ENGLISH_STOP_WORDS


def main():

    l: TFIDFKeywordExtraction = TFIDFKeywordExtraction(stopwords=ENGLISH_STOP_WORDS)

    # load
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle, [l])

    # check whether we have read a Document
    assert doc is not None

    print(l.get_keywords_for_page(0))


if __name__ == "__main__":
    main()
