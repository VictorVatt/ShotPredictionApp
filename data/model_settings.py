from scipy import signal


def LP_filter(x,f_coupure,f_echantillonnage):
    # filtre passe-bas, no phase shift
    b, a = signal.butter(2, f_coupure / (f_echantillonnage / 2), btype='lowpass')
    y = signal.lfilter(b, a, x)
    return y


cols_labels = ["AccXMean", "AccXSD", "AccXSkew", "AccXKurtosis", "AccXMin", "AccXMax", "AccYMean",
               "AccYSD", "AccYSkew", "AccYKurtosis", "AccYMin", "AccYMax", "AccZMean", "AccZSD",
               "AccZSkew", "AccZKurtosis", "AccZMin", "AccZMax", "GyrXMean", "GyrXSD", "GyrXSkew",
               "GyrXKurtosis", "GyrXMin", "GyrXMax", "GyrYMean", "GyrYSD", "GyrYSkew", "GyrYKurtosis",
               "GyrYMin", "GyrYMax", "GyrZMean", "GyrZSD", "GyrZSkew", "GyrZKurtosis", "GyrZMin", "GyrZMax"]

frequence = 60
intervalle = 30 #Intervalle doit pouvoir s'adapter pour le premier et le dernier coup si l'on coupe ou lance trop tot l'enregistrement mais rester à 30 pour le reste des essais
pourcentage_max = 40