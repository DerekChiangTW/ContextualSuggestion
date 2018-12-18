#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from src.utils import *
from scipy.stats import spearmanr, kendalltau

output_dir = 'output'
result_dir = os.path.join(output_dir, 'result')
top10_dir = os.path.join(result_dir, 'top10')
top20_dir = os.path.join(result_dir, 'top20')
top30_dir = os.path.join(result_dir, 'top30')

top30 = get_top30(os.path.join('data', 'top30-award.txt'))
all_users = get_all_users(os.path.join(output_dir, 'all_users.txt'))
all_repos = get_all_repos(os.path.join(output_dir, 'all_repos.txt'))

user2idx = {user: i for i, user in enumerate(all_users)}
repo2idx = {repo: i for i, repo in enumerate(all_repos)}
idx2user = {i: user for i, user in enumerate(all_users)}
user_info = json.load(open(os.path.join(output_dir, 'users_info.json'), 'r'))
repo_info = json.load(open(os.path.join(output_dir, 'repos_info.json'), 'r'))


def save_owned_result(user_list, path):
    with open(path, 'w') as outfile:
        owned = [len(user_info[user]["owned_repos"]) for user in user_list]
        rank = rank_of_list(owned)
        for i in range(len(user_list)):
            outfile.write(",".join([user_list[i], str(owned[i]), str(rank[i])]) + "\n")
    print("Successfully saved file: {}".format(path))


def save_written_result(user_list, path):
    with open(path, 'w') as outfile:
        written = [len(user_info[user]["written_repos"]) for user in user_list]
        rank = rank_of_list(written)
        for i in range(len(user_list)):
            outfile.write(",".join([user_list[i], str(written[i]), str(rank[i])]) + "\n")
    print("Successfully saved file: {}".format(path))


def save_contribution_result(user_list, path):
    with open(path, 'w') as outfile:
        contribution_scores = compute_contribution(output_dir, all_users)
        contributions = [contribution_scores[user] for user in user_list]
        rank = rank_of_list(contributions)
        for i in range(len(user_list)):
            outfile.write(",".join([user_list[i], str(contributions[i]), str(rank[i])]) + "\n")
    print("Successfully saved file: {}".format(path))


def save_fm_result(user_list, path):
    with open(path, 'w') as outfile:
        fm_scores = compute_fm_score(output_dir, all_users, idx2user)
        fm = [fm_scores[user] for user in user_list]
        rank = rank_of_list(fm)
        for i in range(len(user_list)):
            outfile.write(",".join([user_list[i], str(fm[i]), str(rank[i])]) + "\n")
    print("Successfully saved file: {}".format(path))


def load_result(path):
    ranks = []
    with open(path, 'r') as infile:
        for line in infile:
            words = line.rstrip().split(",")
            ranks.append(int(words[2]))
    return ranks


if __name__ == "__main__":

    # preprocess data for FM
    # save_neighbors(output_dir, all_users, repo_info)
    # save_related_repos(output_dir, all_users, user_info)
    # create_fm_train_data(output_dir, all_users, all_repos, user2idx, repo2idx, repo_info)
    # create_fm_test_data(output_dir, all_users, user2idx, repo2idx)

    # save top30 results
    # save_owned_result(top30, os.path.join(top30_dir, 'result_owned.txt'))
    # save_written_result(top30, os.path.join(top30_dir, 'result_written.txt'))
    # save_contribution_result(top30, os.path.join(top30_dir, 'result_commit.txt'))
    # save_fm_result(top30, os.path.join(top30_dir, 'result_wo_fm.txt'))

    # save top20 results
    # top20 = top30[:20]
    # save_owned_result(top20, os.path.join(top20_dir, 'result_owned.txt'))
    # save_written_result(top20, os.path.join(top20_dir, 'result_written.txt'))
    # save_contribution_result(top20, os.path.join(top20_dir, 'result_commit.txt'))
    # save_fm_result(top20, os.path.join(top20_dir, 'result_wo_fm.txt'))

    # save top10 results
    # top10 = top30[:10]
    # save_owned_result(top10, os.path.join(top10_dir, 'result_owned.txt'))
    # save_written_result(top10, os.path.join(top10_dir, 'result_written.txt'))
    # save_contribution_result(top10, os.path.join(top10_dir, 'result_commit.txt'))
    # save_fm_result(top10, os.path.join(top10_dir, 'result_wo_fm.txt'))

    # correct_ranks = list(range(1, 31))
    # path = os.path.join(top30_dir, "result_owned.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top30_dir, "result_written.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top30_dir, "result_commit.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top30_dir, "result_wo_fm.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # correct_ranks = list(range(1, 11))
    # path = os.path.join(top10_dir, "result_owned.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top10_dir, "result_written.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top10_dir, "result_commit.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))

    # path = os.path.join(top10_dir, "result_wo_fm.txt")
    # ranks = load_result(path)
    # print(spearmanr(correct_ranks, ranks))
    # print(kendalltau(correct_ranks, ranks))
    pass
