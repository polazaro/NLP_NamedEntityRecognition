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
                
        #If there the word ends with -ed   
        if str.endswith(word,'ed'):
            # Generate feature name.
            feat_name = "verb_ed::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If there the word ends with -ly      
        if str.endswith(word,'ly'):
            # Generate feature name.
            feat_name = "adverb_ly::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If there is a point anywhere 
        if str.find(word, ".") != -1:
            # Generate feature name.
            feat_name = "points::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is 'to'
        if word == 'to':
            # Generate feature name.
            feat_name = "to_prep::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If any letter is upper (without the initial letter)      
        if len(word)>1 and not str.islower(word[1:]):
            # Generate feature name.
            feat_name = "upper_any::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is 'of'
        if word == 'of':
            # Generate feature name.
            feat_name = "of_prep::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word ends with 'ia'
        if str.endswith(word,'ia'):
            # Generate feature name.
            feat_name = "end_ia::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word ends with 'ing'
        if str.endswith(word,'ing'):
            # Generate feature name.
            feat_name = "end_ing::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is 'from'
        if word == 'from':
            # Generate feature name.
            feat_name = "from_prep::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is a digit
        if str.isdigit(word):
            # Generate feature name.
            feat_name = "isdigit::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is not a digit but contains digits
        if any(char.isdigit() for char in word) and not str.isdigit(word):
            # Generate feature name.
            feat_name = "anydigit::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is 'the'
        if word == 'the':
            # Generate feature name.
            feat_name = "the_art::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word ends with 'ent'
        if str.endswith(word,'ent'):
            # Generate feature name.
            feat_name = "ent_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word is 'in'
        if word == 'in':
            # Generate feature name.
            feat_name = "in_prep::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
                    
        #If the word ends with 'dom'
        if str.endswith(word,'dom'):
            # Generate feature name.
            feat_name = "dom_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'nce'
        if str.endswith(word,'nce'):
            # Generate feature name.
            feat_name = "nce_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ism'
        if str.endswith(word,'ism'):
            # Generate feature name.
            feat_name = "ism_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ist'
        if str.endswith(word,'ist'):
            # Generate feature name.
            feat_name = "ist_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ship'
        if str.endswith(word,'ship'):
            # Generate feature name.
            feat_name = "ship_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ate'
        if str.endswith(word,'ate'):
            # Generate feature name.
            feat_name = "ate_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'fy'
        if str.endswith(word,'fy'):
            # Generate feature name.
            feat_name = "fy_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'en'
        if str.endswith(word,'en'):
            # Generate feature name.
            feat_name = "en_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ize'
        if str.endswith(word,'ize'):
            # Generate feature name.
            feat_name = "ize_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ble'
        if str.endswith(word,'ble'):
            # Generate feature name.
            feat_name = "ble_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'al'
        if str.endswith(word,'al'):
            # Generate feature name.
            feat_name = "al_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ful'
        if str.endswith(word,'ful'):
            # Generate feature name.
            feat_name = "ful_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'y'
        if str.endswith(word,'y') and not str.endswith(word,'fy'):
            # Generate feature name.
            feat_name = "y_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'er'
        if str.endswith(word,'er'):
            # Generate feature name.
            feat_name = "er_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'or'
        if str.endswith(word,'or'):
            # Generate feature name.
            feat_name = "or_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)        
                
        #If the word starts with 'co'
        if str.startswith(word,'co'):
            # Generate feature name.
            feat_name = "co_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'auto'
        if str.startswith(word,'auto'):
            # Generate feature name.
            feat_name = "auto_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
        
        #If the word starts with 'dis'
        if str.startswith(word,'dis'):
            # Generate feature name.
            feat_name = "dis_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'ex'
        if str.startswith(word,'ex'):
            # Generate feature name.
            feat_name = "ex_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'anti'
        if str.startswith(word,'anti'):
            # Generate feature name.
            feat_name = "anti_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'in/im'
        if str.startswith(word,'in') or str.startswith(word,'im') or str.startswith(word,'ir') or str.startswith(word,'il'):
            # Generate feature name.
            feat_name = "not_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'un'
        if str.startswith(word,'un'):
            # Generate feature name.
            feat_name = "un_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'up'
        if str.startswith(word,'up'):
            # Generate feature name.
            feat_name = "up_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word ends with 'trans'
        if str.startswith(word,'trans'):
            # Generate feature name.
            feat_name = "trans_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'en'
        if str.startswith(word,'en'):
            # Generate feature name.
            feat_name = "en_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'de'
        if str.startswith(word,'de'):
            # Generate feature name.
            feat_name = "de_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'com/con'
        if str.startswith(word,'com') or str.startswith(word,'con'):
            # Generate feature name.
            feat_name = "with_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'mis'
        if str.startswith(word,'mis'):
            # Generate feature name.
            feat_name = "mis_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 're'
        if str.startswith(word,'re'):
            # Generate feature name.
            feat_name = "re_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'homo'
        if str.startswith(word,'homo'):
            # Generate feature name.
            feat_name = "homo_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word starts with 'fore'
        if str.startswith(word,'fore'):
            # Generate feature name.
            feat_name = "fore_pref::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
        
        #If the word contains apostrophe
        if str.find(word,"'") != -1:
            # Generate feature name.
            feat_name = "apost::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        #If the word ends with 'acy'
        if str.endswith(word,'acy'):
            # Generate feature name.
            feat_name = "acy_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ity'
        if str.endswith(word,'ity'):
            # Generate feature name.
            feat_name = "ity_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
        
        
        #If the word ends with 'ty'
        if str.endswith(word,'ty') and not str.endswith(word, 'ity'):
            # Generate feature name.
            feat_name = "ty_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ness'
        if str.endswith(word,'ness'):
            # Generate feature name.
            feat_name = "ness_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'sion'
        if str.endswith(word,'sion'):
            # Generate feature name.
            feat_name = "sion_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'tion'
        if str.endswith(word,'tion'):
            # Generate feature name.
            feat_name = "tion_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ise'
        if str.endswith(word,'ise'):
            # Generate feature name.
            feat_name = "ise_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ic'
        if str.endswith(word,'ic'):
            # Generate feature name.
            feat_name = "ic_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ical'
        if str.endswith(word,'ical'):
            # Generate feature name.
            feat_name = "ical_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ous'
        if str.endswith(word,'ous'):
            # Generate feature name.
            feat_name = "ous_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ish'
        if str.endswith(word,'ish'):
            # Generate feature name.
            feat_name = "ish_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'ive'
        if str.endswith(word,'ive'):
            # Generate feature name.
            feat_name = "ive_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)

        #If the word ends with 'less'
        if str.endswith(word,'less'):
            # Generate feature name.
            feat_name = "less_suf::%s" % y_name
            # Get feature ID from name.
            feat_id = self.add_feature(feat_name)
            # Append feature.
            if feat_id != -1:
                features.append(feat_id)
                
        



        return features
		
