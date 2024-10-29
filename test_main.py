# test_main_no_unittest.py
from unittest.mock import patch, MagicMock
import main as main_module
import argparse


def test_create_command():
    with patch("main.create_table") as mock_create_table, patch(
        "main.sqlite3.connect"
    ) as mock_connect, patch("argparse.ArgumentParser.parse_args") as mock_parse_args:

        # 模拟命令行参数
        mock_parse_args.return_value = argparse.Namespace(
            command="create", table_name="test_table"
        )

        # 模拟数据库连接
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        # 调用 main 函数
        main_module.main()

        # 验证 create_table 被正确调用
        assert mock_create_table.called
        assert mock_create_table.call_args[0] == (mock_conn, "test_table")
        assert mock_conn.close.called


def test_query_command():
    with patch("main.query_exec") as mock_query_exec, patch(
        "main.sqlite3.connect"
    ) as mock_connect, patch("argparse.ArgumentParser.parse_args") as mock_parse_args:

        mock_parse_args.return_value = argparse.Namespace(
            command="query", query="SELECT * FROM test_table"
        )
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        main_module.main()

        assert mock_query_exec.called
        assert mock_query_exec.call_args[0] == (mock_conn, "SELECT * FROM test_table")
        assert mock_conn.close.called


def test_delete_command():
    with patch("main.drop_table") as mock_drop_table, patch(
        "main.sqlite3.connect"
    ) as mock_connect, patch("argparse.ArgumentParser.parse_args") as mock_parse_args:

        mock_parse_args.return_value = argparse.Namespace(
            command="delete", delete_query="test_table"
        )
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        main_module.main()

        assert mock_drop_table.called
        assert mock_drop_table.call_args[0] == (mock_conn, "test_table")
        assert mock_conn.close.called


def test_load_command():
    with patch("main.load_data_from_csv") as mock_load_data_from_csv, patch(
        "main.sqlite3.connect"
    ) as mock_connect, patch("argparse.ArgumentParser.parse_args") as mock_parse_args:

        mock_parse_args.return_value = argparse.Namespace(
            command="load",
            table_name="test_table",
            file_path="data/RestaurantReviews.csv",
        )
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        main_module.main()

        assert mock_load_data_from_csv.called
        assert mock_load_data_from_csv.call_args[0] == (
            mock_conn,
            "test_table",
            "data/RestaurantReviews.csv",
        )
        assert mock_conn.close.called


if __name__ == "__main__":
    test_create_command()
    test_query_command()
    test_delete_command()
    test_load_command()
    print("All tests passed!")
