from text_model_class import*
def run_tests():
    """ creates two sources and four samples to compare them to """
    source1 = TextModel('George RR Martin')
    source1.add_file('martin_source_text.txt')
    

    source2 = TextModel('Stephen King')
    source2.add_file('king_source_text.txt')
    

    new1 = TextModel('Core Curriculum Essay')
    new1.add_file('CC_101_paper.txt')
    new1.classify(source1, source2)

    new2 = TextModel('Tolkien')
    new2.add_file('tolkien_sample.txt')
    new2.classify(source1,source2)

    new3 = TextModel('Stephen King Sample')
    new3.add_file('king_sample.txt')
    new3.classify(source1,source2)

    new4 = TextModel('Martin Sample')
    new4.add_file('martin_sample.txt')
    new4.classify(source1,source2)
