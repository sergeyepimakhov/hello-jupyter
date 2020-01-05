from django.test import TestCase

# Create your tests here.

def test_filter_language(self):
    bash1 = '! python main.py'
    bash1_with_trim = ' ! python main.py'
    bash2 = ['%%bash',
             'python main.py']
    bash3 = ['%%sh',
             'python main.py']
    bash4 = ['%env FLASK_APP=quickstart/main.py',
             '%env FLASK_ENV=development',
             '! python -m flask run']

    html1 = ['%%HTML',
             '<h1>Hello</h1>']
    html2 = ['%%html',
             '<h1>Hello</h1>']

    python1 = ['def main():',
               '    print("Hello world!")']
    python2 = ['%%python',
               'def main():',
               '    print("Hello world!")']
    python3 = ['%%python2',
               'def main():',
               '    print("Hello world!")']
    python4 = ['%%python3',
               'def main():',
               '    print("Hello world!")']

    source, code_type = self.mid.define_code_type(bash1)
    assert source == 'python main.py'
    assert code_type == 'bash'

    source, code_type = self.mid.define_code_type(bash1_with_trim)
    assert source == 'python main.py'
    assert code_type == 'bash'

    bash2 = '\n'.join(bash2)
    source, code_type = self.mid.define_code_type(bash2)
    assert source == 'python main.py'
    assert code_type == 'bash'

    bash3 = '\n'.join(bash3)
    source, code_type = self.mid.define_code_type(bash3)
    assert source == 'python main.py'
    assert code_type == 'bash'

    bash4 = '\n'.join(bash4)
    source, code_type = self.mid.define_code_type(bash4)
    assert source.split('\n') == ['export FLASK_APP=quickstart/main.py',
                                  'export FLASK_ENV=development',
                                  'python -m flask run']
    assert code_type == 'bash'

    html1 = '\n'.join(html1)
    source, code_type = self.mid.define_code_type(html1)
    assert source == '<h1>Hello</h1>'
    assert code_type == 'html'

    html2 = '\n'.join(html2)
    source, code_type = self.mid.define_code_type(html2)
    assert source == '<h1>Hello</h1>'
    assert code_type == 'html'

    python1 = '\n'.join(python1)
    source, code_type = self.mid.define_code_type(python1)
    assert source.split('\n') == ['def main():',
                                  '    print("Hello world!")']
    assert code_type == 'python'

    python2 = '\n'.join(python2)
    source, code_type = self.mid.define_code_type(python2)
    assert source.split('\n') == ['def main():',
                                  '    print("Hello world!")']
    assert code_type == 'python'

    python3 = '\n'.join(python3)
    source, code_type = self.mid.define_code_type(python3)
    assert source.split('\n') == ['def main():',
                                  '    print("Hello world!")']
    assert code_type == 'python'

    python4 = '\n'.join(python4)
    source, code_type = self.mid.define_code_type(python4)
    assert source.split('\n') == ['def main():',
                                  '    print("Hello world!")']
    assert code_type == 'python'
