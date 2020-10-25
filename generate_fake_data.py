import textgenrnn as tgr


if __name__ == '__main__':
    textgen = tgr.textgenrnn('ufo_model1_weights.hdf5')
    textgen.generate_samples(temperatures=[0.35, 0.45, .55, .65, .75], return_as_list=False)
