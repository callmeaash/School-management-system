from project import *

def test_main(mocker):
    mock_input = mocker.patch(
        "builtins.input", return_value = 'S'
    )
    mocker.patch("project.fun_students")
    main()
    mock_input.assert_called_once_with("What to you wanna do? ")


def test_show_students(mocker):
    mock_open = mocker.patch(
        "builtins.open", mocker.mock_open(read_data="name,age\nJohn,20")
    )
    mock_print = mocker.patch("builtins.print")
    mocker.patch("project.fun_students")
    show_students()
    mock_open.assert_called_once_with("students.csv")
    assert mock_print.call_count == 1


def test_show_students_file_not_found(mocker):
    mock_open = mocker.patch("builtins.open", side_effect=FileNotFoundError)
    mock_print = mocker.patch("builtins.print")
    mocker.patch("project.fun_students")
    show_students()
    mock_open.assert_called_once_with("students.csv")
    assert mock_print.call_count == 1
    mock_print.assert_called_with(Fore.RED + "No records found!!" + Fore.RESET)


def test_show_teachers(mocker):
    mock_open = mocker.patch(
        "builtins.open", mocker.mock_open(read_data="name,age\nJohn,20")
    )
    mock_print = mocker.patch("builtins.print")
    mocker.patch("project.fun_teachers")
    show_teachers()
    mock_open.assert_called_once_with("teachers.csv")
    assert mock_print.call_count == 1


def test_show_teachers_file_not_found(mocker):
    mock_open = mocker.patch("builtins.open", side_effect=FileNotFoundError)
    mock_print = mocker.patch("builtins.print")
    mocker.patch("project.fun_teachers")
    show_teachers()
    mock_open.assert_called_once_with("teachers.csv")
    assert mock_print.call_count == 1
    mock_print.assert_called_with(Fore.RED + "No records found!!" + Fore.RESET)
