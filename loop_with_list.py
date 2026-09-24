{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyP0sGxgPWhjJ5FoghfwFYbS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Mohit9324/02Saini-Demo/blob/main/loop_with_list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "Count the Word having length greater than 3"
      ],
      "metadata": {
        "id": "P575N5dGWTu5"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vi1_L0vGP5AF",
        "outputId": "92ccb66d-5065-429b-944e-e7c273b441b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'market': 1, 'moved': 1, 'fast': 1, 'today': 1, 'prices': 1, 'went': 1, 'news': 1, 'hard': 1}\n"
          ]
        }
      ],
      "source": [
        "sentences = [\n",
        "    \"the oil market moved fast today\",\n",
        "    \"gas prices went up a lot\",\n",
        "    \"the news hit oil and gas hard\"\n",
        "]\n",
        "word_count = {}\n",
        "for sentence in sentences:\n",
        "    words = sentence.split()\n",
        "\n",
        "    for word in words:\n",
        "        if len(word) > 3:\n",
        "           if word in word_count:\n",
        "              word_count[word] += 1\n",
        "           else:\n",
        "              word_count[word] = 1\n",
        "print(word_count)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "print a dictonary of total pass and fail"
      ],
      "metadata": {
        "id": "nA2iZNVzWdug"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "scores = [45, 78, 92, 33, 88, 60, 25, 95]\n",
        "\n",
        "Total_students = {}\n",
        "\n",
        "for score in scores:\n",
        "   if score >= 50:\n",
        "       Total_students[score] = \"pass\"\n",
        "       continue\n",
        "   else:\n",
        "      Total_students[score] = \"Fail\"\n",
        "\n",
        "print(Total_students)\n",
        "\n",
        "\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uqb2dV_LVrzO",
        "outputId": "3d826b3f-2ea6-4969-fa8e-b08dbb3b3e13"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{45: 'Fail', 78: 'pass', 92: 'pass', 33: 'Fail', 88: 'pass', 60: 'pass', 25: 'Fail', 95: 'pass'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "scores = [45, 78, 92, 33, 88, 60, 25, 95]\n",
        "result = {\"pass\": 0, \"fail\": 0}\n",
        "\n",
        "for score in scores:\n",
        "   if score >= 50:\n",
        "      result[\"pass\"] += 1\n",
        "   else:\n",
        "     result[\"fail\"] += 1\n",
        "\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZYnALCPlZ1wh",
        "outputId": "ffa748a9-8f57-4691-8932-7f5e36e39fd2"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'pass': 5, 'fail': 3}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ballots = [\n",
        "    [\"Alice\", \"Bob\", \"Alice\"],\n",
        "    [\"Bob\", \"Bob\", \"Charlie\"],\n",
        "    [\"Alice\", \"Charlie\", \"Alice\"]\n",
        "]\n",
        "\n",
        "vote_count = {}\n",
        "\n",
        "for round in ballots:\n",
        "    for name in round:\n",
        "       if name in vote_count:\n",
        "          vote_count[name] += 1\n",
        "       else:\n",
        "          vote_count[name] = 1\n",
        "\n",
        "print(vote_count)\n",
        "\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_R9aKb_6cSQJ",
        "outputId": "d32280e4-4f9e-4052-8748-dc048f25c708"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Alice': 4, 'Bob': 3, 'Charlie': 2}\n"
          ]
        }
      ]
    }
  ]
}