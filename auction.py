import pandas as pd

file1 = pd.read_excel('master.xlsx')


OFFSET = 17
LIMIT = 16
VALUES = {}


class Franchise:
    def __init__(self, id_, lst_players=[]):
        self.pl_lst = lst_players
        self.bought_lst = []
        self.value_dict = {}
        self.id = id_
        # check_lst()
        self.num_bought = 0
        self.assign_values()

    def assign_values(self):
        for p_id in values:
            if p_id in self.pl_lst:
                values[p_id] += self.pl_lst.index(p_id) + 1
            else:
                values[p_id] += OFFSET

    def check_lst(self):
        # check for validity
        flag = False
        for pid in self.pl_lst:
            if pid not in values:
                print(f'Player id {pid} is not unsold')
                flag = True
        if flag:
            self.update_list()

    def update_list(self):
        pass

unsold_df = pd.read_excel('Unsold.xlsx')
values = {}
for pid in unsold_df['Id']:
    values[pid] = 0


f = []
df_lst = []
for i in range(1, 9):
    filename = f'l{i}.xlsx'
    df = pd.read_excel(filename, header=None, names=['Id'])
    df_lst.append(df)
    d = df.to_dict()['Id']
    f.append(Franchise(i, list(d.values())))


best_player_id = min(values.items(), key=lambda x: x[1])[0]
print(f'next player id: {best_player_id}')
u_df = unsold_df.drop(unsold_df.index[[best_player_id]])
print(u_df.head(10))
print('----------')
print(unsold_df.head(10))

# def main():
#
#
# if __name__ == '__main__':
#     main()