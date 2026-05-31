from main import main


def test_main_prints_both_lines(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "I love flowers\nhello\n"


def test_main_prints_flowers_line(capsys):
    main()
    assert "I love flowers" in capsys.readouterr().out


def test_main_prints_hello_line(capsys):
    main()
    assert "hello" in capsys.readouterr().out


def test_main_returns_none():
    assert main() is None
