from skseq.sequences.id_feature import IDFeatures
from skseq.sequences.id_feature import UnicodeFeatures

# ----------
# Feature Class
# Extracts features from a labeled corpus (only supported features are extracted
# ----------
class ExtendedFeatures(IDFeatures):

    def add_emission_features(self, sequence, pos, y, features):
        x = sequence.x[pos]
        # Get tag name from ID.
        y_name = self.dataset.y_dict.get_label_name(y)

        # Get word name from ID.
        if isinstance(x, str):
            x_name = x
        else:
            x_name = self.dataset.x_dict.get_label_name(x)

        word = str(x_name)
        # Generate feature name.
        feat_name = "id:%s::%s" % (word, y_name)
        # Get feature ID from name.
        feat_id = self.add_feature(feat_name)
        # Append feature.
        if feat_id != -1:
            features.append(feat_id)

        #Hyphen
        if str.find(word, "-") != -1:
            # Generate feature name.
            feat_name = "hyphen::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If there is a capital letter at the beggining
        if word[0].isupper():
            # Generate feature name.
            feat_name = "upper_ini::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
            
            
        #If it ends with a point
#        if str.endswith(word, "."):
#            # Generate feature name.
#            feat_name = "endpoint::%s" % y_name
#            # Get feature ID from name.
#            feat_id = self.add_feature(feat_name)
#            # Append feature.
#            if feat_id != -1:
#                features.append(feat_id)

#        #If there is an upper letter
#        if not str.islower(word):
#            # Generate feature name.
#            feat_name = "upper::%s" % y_name
#            # Get feature ID from name.
#            feat_id = self.add_feature(feat_name)
#            # Append feature.
#            if feat_id != -1:
#                features.append(feat_id)
                
        #If there is a capital letter at the beggining
        if str.endswith(word,'ed'):
            # Generate feature name.
            feat_name = "verb_ed::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)


        return features
		
