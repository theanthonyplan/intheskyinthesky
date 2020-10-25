import textgenrnn as tgr


ufo_tgr2 = tgr.textgenrnn(name='ufo_model2')
ufo_tgr2.train_from_file('training_data2.txt', new_model=True, batch_size=512, num_epochs=5, rnn_bidirectional=True, rnn_size=64)
ufo_tgr.generate_samples(temperatures=[0.35, 0.45, .55, .65, .75], return_as_list=False)


textgen = textgenrnn('../weights/hacker_news.hdf5')
