

n_vals = 50000
communes_df = pd.read_csv(os.path.join(os.getcwd(), 'data/communes.csv'), header=None)
communes_df.columns = ['name']
communes_df['name'] = communes_df['name'].apply(standardize)

donations = pareto.rvs(1.5, size=communes_df.shape[0])
donations = (donations*10).astype('int')
donations[donations < 20] = 20

communes_sampled = communes_df.loc[:,'name'].sample(n_vals, replace=True, weights=donations).values
communes_with_donation = dict(zip(communes_df.loc[:,'name'].tolist(), donations))
communes_with_donation