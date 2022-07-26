import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from IPython.display import Markdown, display
from aif360.metrics import ClassificationMetric
# from mdss import MDSSClassificationMetric

def default_preprocessing(df):
    df['credit'] = df['credit'].replace({1.0: 0, 2.0: 1})
    return df

def pred_dataset(dataset, model, thresh):
    try:
        # sklearn classifier
        y_val_pred_prob = model.predict_proba(dataset.features)
        pos_ind = np.where(model.classes_ == dataset.favorable_label)[0][0]
    except AttributeError:
        # aif360 inprocessing algorithm
        y_val_pred_prob = model.predict(dataset).scores
        pos_ind = 0

    # make predictions
    y_val_pred = (y_val_pred_prob[:, pos_ind] > thresh).astype(np.float64)

    dataset_pred = dataset.copy()
    dataset_pred.labels = y_val_pred

    return(dataset_pred)


def test(dataset, model, thresh_arr, unprivileged_groups, privileged_groups):
    try:
        # sklearn classifier
        y_val_pred_prob = model.predict_proba(dataset.features)
        pos_ind = np.where(model.classes_ == dataset.favorable_label)[0][0]
    except AttributeError:
        # aif360 inprocessing algorithm
        y_val_pred_prob = model.predict(dataset).scores
        pos_ind = 0
    
    metric_arrs = defaultdict(list)
    bias_scan = defaultdict(list)
    for thresh in thresh_arr:
        y_val_pred = (y_val_pred_prob[:, pos_ind] > thresh).astype(np.float64)

        dataset_pred = dataset.copy()
        dataset_pred.labels = y_val_pred
        metric = ClassificationMetric(
                dataset, dataset_pred,
                unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)

        metric_arrs['thres'].append(thresh_arr[0])
        bal_acc = (metric.true_positive_rate() + metric.true_negative_rate()) / 2
        metric_arrs['bal_acc'].append(1-bal_acc)
        metric_arrs['avg_odds_diff'].append(metric.average_odds_difference())
        metric_arrs['disp_imp'].append(metric.disparate_impact())
        metric_arrs['stat_par_diff'].append(metric.statistical_parity_difference())
        metric_arrs['eq_opp_diff'].append(metric.equal_opportunity_difference())
    
    return metric_arrs


def describe(train=None, val=None, test=None):
    if train is not None:
        display(Markdown("#### Training Dataset shape"))
        print(train.features.shape)
    if val is not None:
        display(Markdown("#### Validation Dataset shape"))
        print(val.features.shape)
    display(Markdown("#### Test Dataset shape"))
    print(test.features.shape)
    display(Markdown("#### Favorable and unfavorable labels"))
    print(test.favorable_label, test.unfavorable_label)
    display(Markdown("#### Protected attribute names"))
    print(test.protected_attribute_names)
    display(Markdown("#### Privileged and unprivileged protected attribute values"))
    print(test.privileged_protected_attributes, 
          test.unprivileged_protected_attributes)
    display(Markdown("#### Dataset feature names"))
    print(test.feature_names)


def plot(x, x_name, y_left, y_left_name, y_left_lim):
    fig, ax1 = plt.subplots(figsize=(10,7))
    ax1.plot(x, y_left)
    ax1.set_xlabel(x_name, fontsize=16, fontweight='bold')
    ax1.set_ylabel(y_left_name, color='b', fontsize=16, fontweight='bold')
    ax1.xaxis.set_tick_params(labelsize=14)
    ax1.yaxis.set_tick_params(labelsize=14)
    ax1.set_ylim(y_left_lim[0], y_left_lim[1])

    # ax2 = ax1.twinx()

    best_ind = np.argmax(y_left)
    # print(thresh_arr[best_ind])
    ax1.axvline(np.array(x)[best_ind], color='k', linestyle=':')
    ax1.grid(True)
    

def plot_acc_fair(x, x_name, y_left, y_left_name, y_right, y_right_name, y_left_lim, y_right_lim):
    fig, ax1 = plt.subplots(figsize=(10,7))
    ax1.plot(x, y_left)
    ax1.set_xlabel(x_name, fontsize=16, fontweight='bold')
    ax1.set_ylabel(y_left_name, color='b', fontsize=16, fontweight='bold')
    ax1.xaxis.set_tick_params(labelsize=14)
    ax1.yaxis.set_tick_params(labelsize=14)
    ax1.set_ylim(y_left_lim[0], y_left_lim[1])

    ax2 = ax1.twinx()
    ax2.plot(x, y_right, color='r')
    ax2.set_ylabel(y_right_name, color='r', fontsize=16, fontweight='bold')
    ax2.set_ylim(y_right_lim[0], y_right_lim[1])

    best_ind = np.argmax(y_left)
    ax2.axvline(np.array(x)[best_ind], color='k', linestyle=':')
    ax2.yaxis.set_tick_params(labelsize=14)
    ax2.grid(True)


### ORIGINAL
# def plot(x, x_name, y_left, y_left_name, y_right, y_right_name, y_left_lim, y_right_lim):
#     fig, ax1 = plt.subplots(figsize=(10,7))
#     ax1.plot(x, y_left)
#     ax1.set_xlabel(x_name, fontsize=16, fontweight='bold')
#     ax1.set_ylabel(y_left_name, color='b', fontsize=16, fontweight='bold')
#     ax1.xaxis.set_tick_params(labelsize=14)
#     ax1.yaxis.set_tick_params(labelsize=14)
#     ax1.set_ylim(y_left_lim[0], y_left_lim[1])

#     ax2 = ax1.twinx()
#     ax2.plot(x, y_right, color='r')
#     ax2.set_ylabel(y_right_name, color='r', fontsize=16, fontweight='bold')
#     if 'DI' in y_right_name:
#         ax2.set_ylim(0., 0.7)
#     else:
#         ax2.set_ylim(y_right_lim[0], y_right_lim[1])

#     best_ind = np.argmax(y_left)
#     ax2.axvline(np.array(x)[best_ind], color='k', linestyle=':')
#     ax2.yaxis.set_tick_params(labelsize=14)
#     ax2.grid(True)


def describe_metrics(metrics, thresh_arr):
    best_ind = np.argmax(metrics['bal_acc'])
    print("Threshold corresponding to Best balanced accuracy: {:6.4f}".format(thresh_arr[best_ind]))
    print("Best balanced accuracy: {:6.4f}".format(metrics['bal_acc'][best_ind]))
    disp_imp_at_best_ind = 1 - min(metrics['disp_imp'][best_ind], 1/metrics['disp_imp'][best_ind])
    print("Corresponding 1-min(DI, 1/DI) value: {:6.4f} (<0.2 is desirable)".format(disp_imp_at_best_ind))
    print("Corresponding average odds difference value: {:6.4f} (closer to 0 is more 'fair')".format(metrics['avg_odds_diff'][best_ind]))
    print("Corresponding statistical parity difference value: {:6.4f} (closer to 0 is more 'fair')".format(metrics['stat_par_diff'][best_ind]))
    print("Corresponding equal opportunity difference value: {:6.4f} (closer to 0 is more 'fair')".format(metrics['eq_opp_diff'][best_ind]))



def test_eta_bal_acc(ETA, dset_raw_trn, dset_raw_vld, dset_raw_tst):

    ## Excerpt From: Aileen Nielsen. “Practical Fairness”.

    pr = PrejudiceRemover(sensitive_attr = 'RACE', eta = ETA)
    scaler = StandardScaler()

    dset_scaled_trn = dset_raw_trn.copy()
    dset_scaled_trn.features = scaler.fit_transform(dset_scaled_trn.features)

    pr_fitted = pr.fit(dset_scaled_trn)

    accs = []
    thresholds = np.linspace(0.01, 0.50, 10)

    dset_val = dset_raw_vld.copy()
    dset_val.features = scaler.transform(dset_val.features)

    ############# STEP 1 TRAINING WITH IN-PROCESSING ####
    pr_pred_prob = pr_fitted.predict(dset_val).scores

    ############# STEP 2 PICKING THRESHOLD WITH VALIDATION DATA ####
    for threshold in thresholds:
        dset_val_pred = dset_val.copy()
        dset_val_pred.labels = (pr_pred_prob[:, 0] > threshold).astype(np.float64)

        metric = ClassificationMetric(
                    dset_val, dset_val_pred,
                    unprivileged_groups = unpriv_group,
                    privileged_groups=priv_group)
        accs.append((metric.true_positive_rate() + \
                     metric.true_negative_rate()) / 2)

    pr_val_best_idx = np.argmax(accs)
    best_threshold = thresholds[pr_val_best_idx]

    ######### STEP 3 TEST DATA ####
    dset_tst = dset_raw_tst.copy()
    dset_tst.features = scaler.transform(dset_tst.features)

    pr_pred_prob = pr_fitted.predict(dset_tst).scores


    dset_tst_pred = dset_tst.copy()
    dset_tst_pred.labels = (pr_pred_prob[:, 0] > best_threshold).astype(np.float64)

    metric = ClassificationMetric(
                dset_tst, dset_tst_pred,
                unprivileged_groups = unpriv_group,
                privileged_groups   = priv_group)
    test_acc = (metric.true_positive_rate() + metric.true_negative_rate()) / 2
    test_disp_impact = metric.disparate_impact()

    print("Testing accuracy with ETA %0.2f = %0.2f Disparate impact %0.2f" % (ETA, test_acc, test_disp_impact))
    
    return (test_acc, test_disp_impact)

